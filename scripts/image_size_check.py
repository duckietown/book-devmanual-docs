import os
import sys
import json
from pathlib import Path
import imagesize
from typing import Dict, Tuple, Set, Optional, List
from bs4 import BeautifulSoup


# if the source images are as this times as big as images in HTMLs, warnings will be generated
CONST_IMAGE_OVERSIZE_MIN_RATIO = 2.0
# show each src image size and sizes for html usage
CONST_DETAILS_PRINT = True


def get_image_path_with_sizes(directory_path: str) -> Dict[str, Tuple[float, float]]:
    """Obtain image files in the given directory and the respective sizes

    Args:
        directory_path (str): path in which directory to look for images

    Returns:
        Dict[str, Tuple[int, int]]: image paths as keys, and (width, height) tuples as values
    """

    ret = {}
    for dirpath, lst_dirs, lst_files in os.walk(directory_path):
        for fname in lst_files:
            f_path = os.path.join(dirpath, fname)
            width, height = imagesize.get(f_path)
            if width == -1 or height == -1:
                continue  # not an image file
            ret[os.path.relpath(f_path)] = (float(width), float(height))

    return ret


def parse_html_style_attribute(
    style_str: str,
    interested_keys: Set[str],
) -> Dict[str, str]:
    """
    style_str is the string at style attribute in an HTML tag.
    e.g. <... style="width: 10px; height: 20px;" .../> 

    Returns a dictionary containing string values for interested_keys if present
    """

    ret = {}

    for chunk in style_str.strip().split(';'):
        try:
            splitted = chunk.strip().split(':')
            assert len(splitted) == 2
            key, val = map(lambda s: s.strip(), splitted)
            if key in interested_keys:
                ret[key] = val
        except Exception as e:
            # print(f"Error parsing style value for '{chunk}'. Error: {e}")
            pass

    return ret


def _parse_width_height(style_obj: Dict[str, str]) -> Tuple[float, float]:
    width = height = -1  # indicate no such attribute found

    width_str = style_obj.get("width")
    height_str = style_obj.get("height")

    # TODO: for none px values?
    if width_str is not None:
        width = float(width_str.replace("px", ""))

    if height_str is not None:
        height = float(height_str.replace("px", ""))

    return width, height


def _keep_max_image_size(
    lst_sizes: Set[Tuple[float, float]],
    width: float,
    height: float,
):
    # existing
    if (width, height) in lst_sizes:
        return lst_sizes

    ret = set([(width, height)]).union(lst_sizes)
    for w, h in lst_sizes:
        if width >= w and height >= h:
            # no need to keep current (w, h)
            ret.remove((w, h))
            continue
        if w >= width and h >= width:
            # no need to add given width&height
            ret.remove((width, height))
            break

    return ret


def _comp_html_and_src_image_sizes(
    src_img_path: str,
    html_size: Tuple[float, float],
    src_size: Tuple[float, float],
    oversize_min_ratio: float = 2.0,
) -> bool:
    """
    Compare and warn user if src image is at least as oversize_min_ratio times big as html img
    """

    is_too_large = (
        html_size[0] * oversize_min_ratio <= src_size[0]
        and html_size[1] * oversize_min_ratio <= src_size[1]
    )
    if is_too_large:
        print(f"\t- {os.path.relpath(src_img_path)}")
        return True
    
    return False


def compare_html_image_sizes(
    build_html_path: str,
    src_file_path: str,
    oversize_min_ratio: float,
    show_extra_details: bool,
):
    """
    Compare <img> and actual image size and issue warnings if actual image is much bigger
    """

    # get src image sizes
    img_sizes = get_image_path_with_sizes(src_file_path)

    # TODO: 2 src images named the same, how do they appear in html/ folder?
    # filename: [(w1, h1), (w2, h2), ...] if used multiple times
    html_imgs = {}

    # lst_html = []
    for path in Path(build_html_path).rglob("*.html"):
        # print(path.absolute())
        # lst_html += path.name
        with open(path.absolute(), 'r') as f_html:
            # parse html to find <img> tags
            html_content = f_html.read()
            soup = BeautifulSoup(html_content, "html.parser")
            images = soup.find_all("img")
            for pic in images:
                pic_src = str(pic["src"])
                # if web source, ignore source
                if pic_src.startswith(("http://", "https://")):
                    continue

                pic_path, pic_name = os.path.split(pic_src)
                if pic_name not in html_imgs:
                    html_imgs[pic_name] = set()

                # retrieve width/height px values
                pic_style: str = pic.get("style")  # jupyter-book generated images use this attribute
                style_obj = None
                if pic_style is not None:
                    style_obj = parse_html_style_attribute(pic_style, interested_keys=["width", "height"])
                    width, height = _parse_width_height(style_obj)
                    if not width == -1 or not height == -1:  # has at least valid width/height
                        # print(path.name, pic_name, f"({width}, {height})")
                        html_imgs[pic_name] = _keep_max_image_size(html_imgs[pic_name], width=width, height=height)
                        # print(html_imgs)
    
    # match html_img sizes with src image file sizes

    # print(html_imgs)
    html_imgs_max = {}
    # obtain max width and height for each image
    for fname, set_sizes in html_imgs.items():
        if len(set_sizes) == 0:
            continue
        max_w = max([_w for _w, _ in set_sizes])
        max_h = max([_h for _, _h in set_sizes])
        html_imgs_max[fname] = (max_w, max_h)

    # print(img_sizes)
    img_name_sizes = {}
    for fname, sizes in img_sizes.items():
        img_name_sizes[os.path.split(fname)[-1]] = (sizes, fname)

    # check if src is too big
    print((
        f"These source images are at least {oversize_min_ratio} "
        "times as big as all height and width use cases in all HTMLs. "
        "Please consider shrink the source image before pushing.\n"
    ))

    stats_total = len(img_name_sizes)
    stats_cnt_oversized = 0
    stats_cnt_unmatched = 0
    for fname, src_img_data in img_name_sizes.items():
        d_html = html_imgs_max.get(fname)
        src_sizes, src_img_path = src_img_data
        if d_html is None:
            # print(f"No match in HTMLs found for source image: {src_img_path}")  # this could be logos, favicon, etc.
            stats_cnt_unmatched += 1
            continue

        is_too_large = _comp_html_and_src_image_sizes(
            src_img_path=src_img_path,
            html_size=d_html,
            src_size=src_sizes,
            oversize_min_ratio=oversize_min_ratio,
        )
        if is_too_large:
            stats_cnt_oversized += 1
    
    # stats
    print()
    print("*" * 80)
    print("Stats:")
    print("\t-", f"{stats_cnt_oversized} / {stats_total} source images are oversized!")
    # print("\t-", f"{stats_cnt_unmatched} / {stats_total} source images did not find a match in built html.")

    # debug print
    if show_extra_details:
        print("=" * 80)
        print("Details")

        print("-" * 80)
        print("Image sizes in HTMLs")
        print(json.dumps(html_imgs, indent=2, cls=SetEncoder))
        # print(html_imgs)

        print("-" * 80)
        print("Source image sizes")
        print(json.dumps(img_sizes, indent=2, cls=SetEncoder))
        # print(img_sizes)


class SetEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, set):
            return list(obj)
        return json.JSONEncoder.default(self, obj)

if __name__ == "__main__":
    src_path = sys.argv[1]
    html_path = sys.argv[2]

    # print(f"Processing for folder: {html_path}")
    compare_html_image_sizes(
        build_html_path=html_path,
        src_file_path=src_path,
        oversize_min_ratio=CONST_IMAGE_OVERSIZE_MIN_RATIO,
        show_extra_details=CONST_DETAILS_PRINT,
    )

    # print(get_image_path_with_sizes(src_path))

    """Testing"""