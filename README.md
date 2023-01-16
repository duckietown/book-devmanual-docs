# Template: template-book

This template provides a boilerplate repository for books in Duckietown.

## What to change

### Placeholders in `src/_config.yml`
TODO

### Structure in `src/_toc.yml`
TODO

### Logo in `src/logo.png`
TODO

## Build

You can build this book by running the command,

```shell
jb build --path-output ./html/ ./src/
```

TODO: wrap this with `dts docs build`.


## Other TODOs
* Image size warning: the idea is, if the image in html has a size that is way smaller than the original source image, warn the user.
    1. Problem: if using images `images/im.png`, and `imgs/im.png`, these source images will be copied to the `_build/html/_images` with names `im.png` and `im1.png`. So the original idea of parsing HTML (bs4) for obtaining included image file and size is not valid. Because there is not a way to match the renamed images back to source images.
    1. Problem: for non px values?


## Temp notes
### Use of image size check script
#### How-to run
```bash
# in repository root
python3 scripts/image_size_check.py $(pwd)/src $(pwd)/html/_build/html
```
#### Example outcome
```bash
These source images are at least 2.0 times as big as all height and width use cases in all HTMLs. Please consider shrink the source image before pushing.

        - src/images/image.png

********************************************************************************
Stats:
        - 1 / 3 source images are oversized!
================================================================================
Details
--------------------------------------------------------------------------------
Image sizes in HTMLs
{
  "logo.png": [],
  "image.png": [
    [
      -1,
      150.0
    ],
    [
      63.0,
      47.2
    ]
  ]
}
--------------------------------------------------------------------------------
Source image sizes
{
  "src/logo.png": [
    840.0,
    859.0
  ],
  "src/images/favicon.ico": [
    512.0,
    512.0
  ],
  "src/images/image.png": [
    630.0,
    472.0
  ]
}
```