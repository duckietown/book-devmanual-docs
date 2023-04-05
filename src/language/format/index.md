---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

```{note}
This is a shortlisted version of the [MyST syntax cheat sheet](https://jupyterbook.org/en/stable/reference/cheatsheet.html).
```

(myst_cheatsheet)=
# MyST syntax cheat sheet

## Headers

``````{list-table}
:header-rows: 1
:widths: 20 15 15

* - Syntax
  - Example
  - Result
* - ```md
    # Heading level 1
    ## Heading level 2
    ### Heading level 3
    #### Heading level 4
    ##### Heading level 5
    ###### Heading level 6
    ```
  - ```md
    # MyST syntax cheat sheet
    ```
  - Level 1-6 headings, denoted by number of `#`
``````

## Target headers

``````{list-table}
:header-rows: 1
:widths: 20 15 15

* - Syntax
  - Example
  - Result
* - ```md
    (target_header)=
    ```
  - ```md
    (myst_cheatsheet)=
    # MyST Cheat Sheet
    ```
  - See [below](ref/target_headers) how to reference target headers.
``````

(ref/target_headers)=
### Referencing target headers

<!-- Targets can be referenced with the [ref inline role](https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html#role-ref) which uses the section title by default: -->

```md
[](myst_cheatsheet)
```

You can specify the text of the target:

```md
[MyST syntax lecture](myst_cheatsheet)
```

## Quote

``````{list-table}
:header-rows: 1
:widths: 20 20 10

* - Syntax
  - Example
  - Result
* - ```md
    > text
    ```
  - ```md
    > this is a quote
    ```
  - quoted text
``````

## Thematic break

``````{list-table}
:header-rows: 1
:widths: 20 15 15

* - Syntax
  - Example
  - Result
* - ```md
    ---
    ```
  - ```md
    This is the end of some text.

    ---

    ## New Header
    ```
  - Creates a horizontal line in the output
``````

## Line comment

``````{list-table}
:header-rows: 1
:widths: 20 15 15

* - Syntax
  - Example
  - Result
* - ```md
    % text
    ```
  - ```md
    a line
    % a comment
    another line
    ```
  - See [Comments](https://myst-parser.readthedocs.io/en/latest/using/syntax.html#syntax-comments) for more information.
``````

## Block break

``````{list-table}
:header-rows: 1
:widths: 20 15 15

* - Syntax
  - Example
  - Result
* - ```md
    +++
    ```
  - ```md
    This is an example of
    +++ {"meta": "data"}
    a block break
    ```
  - This is an example of
    +++ {"meta": "data"}
    a block break
``````

## HTML block

``````{list-table}
:header-rows: 1
:widths: 20 15 15

* - Syntax
  - Example
  - Result
* - ```html
    <tagName> text <tagName>
    ```
  - ```html
    <p> This is a paragraph </p>
    ```
  - <p> This is a paragraph </p>
``````

## Links

``````{list-table}
:header-rows: 1
:widths: 20 20 10

* - Syntax
  - Example
  - Result
* - ```md
    [text](target)
    ```
  - ```md
    [Jupyter Book](https://jupyterbook.org)
    ```
  - [Jupyter Book](https://jupyterbook.org)
* - ```md
    [text](relative_path)
    ```
  - ```md
    [Another page](../style/index)
    ```
  - [Another page](../style/index)
* - ```md
    <target>
    ```
  - ```md
    <https://jupyterbook.org>
    ```
  - <https://jupyterbook.org>
* - ```md
    [text][key]
    ```
  - ```md
    [Jupyter Book][intro_page]

    [intro_page]: https://jupyterbook.org
    ```
  - [Jupyter Book][intro_page]

    [intro_page]: https://jupyterbook.org
``````

## Lists

### Ordered list

``````{list-table}
:header-rows: 1
:widths: 20 20

* - Example
  - Result
* - ```md
    1. First item
    2. Second item
        1. First sub-item
    ```
  - 1. First item
    2. Second item
        1. First sub-item
* - ```md
    1. First item
    2. Second item
        * First sub-item
    ```
  - 1. First item
    2. Second item
        * First subitem
``````

### Unordered list

``````{list-table}
:header-rows: 1
:widths: 20 20

* - Example
  - Result
* - ```md
    * First item
    * Second item
      * First subitem
    ```
  - * First item
    * Second item
      * First subitem
* - ```md
    * First item
      1. First subitem
      2. Second subitem
    ```
  - * First item
      1. First subitem
      2. Second subitem
``````

## Tables

``````{list-table}
:header-rows: 1
:widths: 20 20 20

* - Syntax
  - Example
  - Result
* - ```md
    | a    | b    |
    | :--- | ---: |
    | c    | d    |
    ```
  - ```md
    |    Training   |   Validation   |
    | :------------ | -------------: |
    |        0      |        5       |
    |     13720     |      2744      |
    ```
  - |    Training   |   Validation   |
    | :------------ | -------------: |
    |        0      |        5       |
    |     13720     |      2744      |
* - ````md
    ```{list-table} Table title
    :header-rows: 1
    :name: label-to-reference

    * - Col1
      - Col2
    * - Row1 under Col1
      - Row1 under Col2
    * - Row2 under Col1
      - Row2 under Col2
    ```
    ````
  - ````md
    ```{list-table} This table title
    :header-rows: 1
    :name: example-table

    * - Training
      - Validation
    * - 0
      - 5
    * - 13720
      - 2744
    ```
    ````
  - ```{list-table} This table title
    :header-rows: 1
    :name: example-table

    * - Training
      - Validation
    * - 0
      - 5
    * - 13720
      - 2744
    ```
``````

### Referencing tables

```{note}
In order to reference a table, you must add a label to it.
To add a label to your table simply include a `:name:` parameter followed by the label of your table.
In order to add a *numbered reference*, you
must also include a table title. See example above.
```

``````{list-table}
:header-rows: 1
:widths: 10 20 20

* - Syntax
  - Example
  - Result
* - ```md
    {numref}`label`
    ```
  - ```md
    {numref}`example-table` is an example.
    ```
  - {numref}`example-table` is an example.
* - ```md
    [text](label)
    ```
  - ```md
    This is an unnumbered ref: [table](example-table).
    ```
  - This is an unnumbered ref: [table](example-table).
``````

## Tabs

Tabs can be used in several ways:
1) At the page level to enclose instruction versions related to different releases (for example, to separate the DB19 and DB21 assembly instructions).
2) Within pages to divide duplicate content with tab based.
3) Nested within other components such as a list.

```{note}
Related content that does not include some duplication should be shown in a table rather than a tab to prevent hidden text.
```

``````{list-table}
:header-rows: 1
:widths: 20 20

* - Example
  - Result
* - `````md
    ````{tab-set}
    
    ```{tab-item} DB19
    This is example content for the DB19
    ```
    
    ```{tab-item} DB21
    This is example content for the DB21
    ```
    ````
    `````
    
  - ````{tab-set}
    
    ```{tab-item} DB19
    This is example content for the DB19
    ```
    
    ```{tab-item} DB21
    This is example content for the DB21
    ```
    ````
``````

## Admonitions

``````{list-table}
:header-rows: 1
:widths: 1 20

* - Syntax
  - Result
* - ````md
    ```{note}
    Use note directives for basic highlighting.
    ```
    ````
  - ```{note}
    Use note directives for basic highlighting.
    ```
* - ````md
    ```{warning}
    Use warnings for situations that might 
    cause harm, but can be fixed.
    ```
    ````
  - ```{warning}
    Use warnings for situations that might cause harm, but can be fixed.
    ```
* - ````md
    ```{tip}
    A tip is a useful suggestion for the reader.
    ```
    ````
  - ```{tip}
    A tip is a useful suggestion for the reader.
    ```
* - ````md
    ```{attention}
    This directive should be used to
    highlight particularly tricky steps.
    ```
    ````
  - ```{attention}
    This directive should be used to highlight particularly tricky steps.
    ```
* - ````md
    ```{danger}
    Used for situations that might 
    cause irreparable harm (to people or robots).
    ```
    ````
  - ```{danger}
    Used for situations that might cause irreparable harm (to people or robots).
    ```
* - ````md
    ```{seealso}
    Used for external links (to
    third-party websites or other documents).
    ```
    ````
  - ```{seealso}
    Used for external links (to third-party websites or other documents).
    ```
``````

All above specific admonitions are specific pre-made directives.
You could make an admonition with custom title and class with the example below.

``````{list-table}
:header-rows: 1
:widths: 10 20 20

* - ````md
    ```{admonition} Title
    text
    ```
  - ````md
    ```{admonition} General admonition
    content
    ```
    ````
  - ```{admonition} General admonition
    content
    ```
* - ````md
    ```{admonition} Title
    :class: warning
    text
    ```
    ````
  - ````md
    ```{admonition} This is a title
    :class: warning
    A custom admonition
    ```
    ````
  - ```{admonition} This is a title
    :class: warning
    A custom admonition
    ```
``````

## Icons

Icons are provided by the [font-awesome](https://fontawesome.com/) project.
The complete list of icons available can be found [here](https://fontawesome.com/v5/search?o=r&m=free).

``````{list-table}
:header-rows: 1
:widths: 10 20 20

* - Syntax
  - Example
  - Result
* - ````md
    ```{icon} <icon-id>
    ```
    ````
  - ````md
    ```{icon} ice-cream
    ```
    ````
  - ```{icon} ice-cream
    ```
    
``````

## Figures

``````{list-table}
:header-rows: 1
:widths: 10 20 20

* - Syntax
  - Example
  - Result
* - ````md
    ```{figure} ./path/to/figure.jpg
    :name: label

    caption
    ```
    ````
  - ````md
    ```{figure} ../../_images/duckietown.jpeg
    :width: 50px
    :name: figure-example-2

    Here is my figure caption!
    ```
    ````
  - ```{figure} ../../_images/duckietown.jpeg
    :width: 50px
    :name: figure-example-2

    Here is my figure caption!
    ```
* - ````md
    ```{image} ./path/to/figure.jpg
    :name: label
    ```
    ````
  - ````md
    ```{image} ../../_images/duckietown.jpeg
    :scale: 20%
    :align: center
    :name: image-example
    ```
    ````
  - ```{image} ../../_images/duckietown.jpeg
    :scale: 20%
    :align: center
    :name: image-example
    ```
* - ````md
    ![alt-text](path/to/image)
    ````
  - ````md
    ![](https://tinyurl.com/39ewhkab)
    ````
  - ![](https://tinyurl.com/39ewhkab)
    
``````

### Framed figures

Use the `:class: framed` parameter to add a border around the image.

``````{list-table}
:header-rows: 1
:widths: 10 20 20

* - Syntax
  - Example
  - Result
* - ````md
    ```{figure} ./path/to/figure.jpg
    :class: framed
    ```
    ````
  - ````md
    ```{figure} ../../_images/duckietown.jpeg
    :width: 50px
    :class: framed
    ```
    ````
  - ```{figure} ../../_images/duckietown.jpeg
    :width: 50px
    :class: framed
    ```
    
``````

:::{note}
* Content/caption is not permitted for *image*s, but only available for *figure*s.
* Settings are not available with `![alt-text](path/to/image)` format
  :::

<!-- See {doc}`../content/figures` and {doc}`../file-types/markdown` for more information. -->

### Referencing figures

``````{list-table}
:header-rows: 1
:widths: 10 20 20

* - Syntax
  - Example
  - Result
* - ```md
    {numref}`label`
    ```
  - ```md
    {numref}`figure-example-2`is a
    figure example.
    ```
  - {numref}`figure-example-2` is a
    figure example.
* - ```md
    {numref}`text %s <label>`
    ```
  - ```md
    {numref}`Figure %s <figure-example-2>`
    is an example.
    ```
  - {numref}`Figure %s <figure-example-2>`
    is an example.
* - ```md
    [text]<label>
    ```
  - ```md
    This [figure](figure-example-2)
    is an example.
    ```
  - This [figure](figure-example-2)
    is an example.
``````

### Referencing images

``````{list-table}
:header-rows: 1
:widths: 15 20 15

* - Syntax
  - Example
  - Result
* - ```md
    [text](label)
    ```
  - ```md
    This [image](image-example)
    is an example.
    ```
  - This [image](image-example)
    is an example.
``````

## Videos

Videos can be referenced using the following methods:

1) `vimeo` - When possible, video content should be added to the Vimeo account and formatted with the custom Duckietown `vimeo` directive.  
2) `videoembed` - For other video content accessible via a web link, use the `videoembed` directive. All [`iframe` attributes](https://www.w3schools.com/tags/tag_iframe.ASP) are available mimicking the `:alt:` parameter syntax below.
3) `video` - For videos stored locally to the book project (this is not recommended), use the `video` directive. All [`iframe` attributes](https://www.w3schools.com/tags/tag_video.asp) are available mimicking the `:alt:` parameter syntax below.


### Referencing Vimeo videos

``````{list-table}
:header-rows: 1
:widths: 15 20 15

* - Syntax
  - Example
  - Result
* - ````md
    ```{vimeo} video-id
    :alt: alt text
    ```
    ````
  - ````md
    ```{vimeo} 527022343
    :alt: alt text
    ```
    ````
  - ```{vimeo} 527022343
    :alt: alt text
    ```
``````

### Referencing web videos

``````{list-table}
:header-rows: 1
:widths: 15 20 15

* - Syntax
  - Example
  - Result
* - ````md
    ```{video} embed_link
    :alt: alt text
    ```
    ````
  - ````md
    ```{video} https://www.youtube.com/embed/mXH1u885bn8
    :alt: alt text
    ```
    ````
  - 
``````

### Referencing local videos

This is not recommended - please host your video content on Vimeo or another online service rather than in the book project.  If absolutely necessary, you can include local videos with custom formatting using the `video` directive.

Supported file types: `.mp4`, `.ogm`, `.ogv`, `.ogg`, `.webm`.

``````{list-table}
:header-rows: 1
:widths: 15 20 15

* - Syntax
  - Example
  - Result
* - ````md
    ```{video} file_path 
    :alt: alt
    ```
    ````
  - ````md
    ```{video} ../assets/videos/my_video.mp4
    :alt: alt text
    ```
    ````
  -
``````

## Math

``````{list-table}
:header-rows: 1
:widths: 10 20 20

* - Syntax
  - Example
  - Result
* - Inline
  - ```md
    This is an example of an
    inline equation $z=\sqrt{x^2+y^2}$.
    ```
  - This is an example of an
    inline equation $z=\sqrt{x^2+y^2}$.
* - Math blocks
  - ```md
    This is an example of a
    math block

    $$
    z=\sqrt{x^2+y^2}
    $$
    ```
  - This is an example of a
    math block

    $$
    z=\sqrt{x^2+y^2}
    $$
* - Math blocks with labels
  - ```md
    This is an example of a
    math block with a label

    $$
    z=\sqrt{x^2+y^2}
    $$ (eq-label)
    ```
  - This is an example of a
    math block with a label

    $$
    z=\sqrt{x^2+y^2}
    $$ (eq-label)
``````

### Referencing math directives

``````{list-table}
:header-rows: 1
:widths: 15 20 15

* - Syntax
  - Example
  - Result
* - ```md
    [](label)
    ```
  - ```md
    Check out equation [](eq-label).
    ```
  - Check out equation [](eq-label).
``````

## Code

### In-line code

**Example**:

```md
Wrap in-line code blocks in backticks: `boolean example = true;`.
```

**Result**:

Wrap in-line code blocks in backticks: `boolean example = true;`.

### Code and syntax highlighting

**Example**:

````md
```python
note = "Python syntax highlighting"
print(node)
```
````

or

````md
```none
No syntax highlighting.
```
````

**Result**:

```python
note = "Python syntax highlighting"
print(node)
```

or

```none
No syntax highlighting.
```

### Executable code

````{warning}
Make sure to include this front-matter YAML block at the beginning of your `.ipynb` or `.md` files.
```
---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---
```
````

**Example**:

````md
```{code-cell} ipython3
note = "Python syntax highlighting"
print(note)
```
````

**Result**:

```{code-cell} ipython3
note = "Python syntax highlighting"
print(note)
```

(myst_cheatsheet:code-cell:tags)=
#### Tags

See the [tags section on Jupyter Books documentation](https://jupyterbook.org/en/stable/reference/cheatsheet.html#tags). For formatting the code cells.

### Gluing variables

**Example**:

``````md
```{code-cell} ipython3
from myst_nb import glue
my_variable = "here is some text!"
glue("glued_text", my_variable)
```

Here is an example of how to glue text: {glue:}`glued_text`
``````

**Result**:

```{code-cell} ipython3
from myst_nb import glue
my_variable = "here is some text!"
glue("glued_text", my_variable)
```

Here is an example of how to glue text: {glue:}`glued_text`

<!-- See {ref}`glue/gluing` for more information. -->

### Gluing numbers

**Example**:

``````md
```{code-cell} ipython3
from myst_nb import glue
import numpy as np
import pandas as pd

ss = pd.Series(np.random.randn(4))
ns = pd.Series(np.random.randn(100))

glue("ss_mean", ss.mean())
glue("ns_mean", ns.mean(), display=False)
```

Here is an example of how to glue numbers: {glue:}`ss_mean` and {glue:}`ns_mean`.
``````

**Result**:

```{code-cell} ipython3
from myst_nb import glue
import numpy as np
import pandas as pd

ss = pd.Series(np.random.randn(4))
ns = pd.Series(np.random.randn(100))

glue("ss_mean", ss.mean())
glue("ns_mean", ns.mean(), display=False)
```

Here is an example of how to glue numbers: {glue:}`ss_mean` and {glue:}`ns_mean`.

<!-- See {ref}`glue/gluing` for more information. -->

### Gluing visualizations

**Example**:

``````md
```{code-cell} ipython3
from myst_nb import glue
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 200)
y = np.sin(x)
fig, ax = plt.subplots()
ax.plot(x, y, 'b-', linewidth=2)

glue("glued_fig", fig, display=False)
```

This is an inline glue example of a figure: {glue:}`glued_fig`.
This is an example of pasting a glued output as a block:
```{glue:} glued_fig
```
``````

**Result**:

```{code-cell} ipython3
from myst_nb import glue
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 200)
y = np.sin(x)
fig, ax = plt.subplots()
ax.plot(x, y, 'b-', linewidth=2)

glue("glued_fig", fig, display=False)
```

This is an inline glue example of a figure: {glue:}`glued_fig`.
This is an example of pasting a glued output as a block:

```{glue:} glued_fig
```

<!-- See {ref}`glue/gluing` for more information. -->

### Gluing math

**Example**:

``````md
```{code-cell} ipython3
import sympy as sym
x, y = sym.symbols('x y')
z = sym.Function('z')
z = sym.sqrt(x**2+y**2)
glue("example_eq", z, display=False)
```

To glue a math equation try
```{glue:math} example_eq
:label: glue-eq-example
```
``````

**Result**:

```{code-cell} ipython3
import sympy as sym
x, y = sym.symbols('x y')
z = sym.Function('z')
z = sym.sqrt(x**2+y**2)
glue("example_eq", z, display=False)
```

To glue a math equation try:

```{glue:math} example_eq
:label: glue-eq-example
```

## Reference documents

``````{list-table}
:header-rows: 1
:widths: 10 20 20

* - Syntax
  - Example
  - Result
* - ```md
    [](path/to/document)
    ```
  - ```md
    Ref to [](../style/index)
    ```
  - Ref to [](../style/index)
* - ```md
    [text](path/to/document)
    ```
  - ```md
    See [here](../style/index)
    for more information.
    ```
  - See [here](../style/index)
    for more information.
``````

### Cross-book references

The cross-book referencing is achieved using the 
[intersphinx](https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html)
plugin for sphinx.
For a cross-book reference, you need to know the book name and the label defined within that book.

```{note}
All books hosted on `docs.duckietown.com` are automatically made available to be linked from any
other Duckietown book. The book name is the repository name.
```

#### Example

```{example}
Link to a [page on another book](book-opmanual-duckiebot:duckiebot-boot).
```

#### How to configure

The mapping between book names and their remote location is defined in the `_config.yml` file.
For example, we can add a link to the book `jupyter-book-docs` as follows,

```yaml
sphinx:
  ...
  config:
    intersphinx_mapping:
      jupyter-book-docs:
        - "https://jupyterbook.org/en/stable"
        - null
```

````{admonition} Advanced: list all labels for a given book
:class: dropdown

To conveniently find the available labels in other books, a utility comes with jupyter-book installation.
Take the above linked book for example:

```bash
python -m sphinx.ext.intersphinx https://jupyterbook.org/en/stable/objects.inv
```

Or, use it in a script (example outcomes provided below)

```python
from sphinx.ext.intersphinx import inspect_main
inspect_main(["https://jupyterbook.org/en/stable/objects.inv"])
```

````


## Footnotes

``````{margin}
```{note}
Footnotes are displayed at the very bottom of the page.
```
``````

``````{list-table}
:header-rows: 1
:widths: 20 20 10

* - Syntax
  - Example
  - Result
* - ```md
    [^ref]

    [^ref]: Footnote text
    ```
  - ```md
    This is a footnote reference.[^myref]

    [^myref]: This **is** the footnote definition.
    ```
  - This is a footnote reference.[^myref]
``````

[^myref]: This **is** the footnote definition.


(language-format-troubleshooting)=
## Troubleshooting

Troubleshooting cards can be created using the `{trouble}` directive.

``````{list-table}
:header-rows: 1
:widths: 6 20

* - Syntax
  - Example
* - ````md
    ```{trouble}
    symptom here
    ---
    resolution here
    ```
    ````
  - ```{trouble}
    I do not see a camera image.
    ---
    Make sure the camera cable is plugged in.
    ```
``````

(language-format-requirements)=
## Requirements

Requirements/outputs cards can be created using the `{needget}` directive.

``````{list-table}
:header-rows: 1
:widths: 6 20

* - Syntax
  - Example
* - ````md
    ```{needget}
    * Requirement 1
    * Requirement 2
    ---
    * Output 1
    ```
    ````
  - ```{needget}
    * Duckie
    * Robot
    ---
    * Duckiebot
    ```
``````

## Tests

You can use the Test / What to Expect card (`testexpect`) to define checkpoints after book instructions.

``````{list-table}
:header-rows: 1
:widths: 10 20

* - Syntax
  - Result
* - ````md
    ```{testexpect}
    Test
    ---
    Expect
    ```
    ````
  - ```{testexpect}
    ```bash
    pip3 --version
    ---
    This command should output a version number for the `pip3` package.
    ```
``````

(language-format-todo)=
## ToDos

You can drop **ToDos** throughout the documentation using the `{todo}` directive.
ToDos are rendered only on the staging documentation, they are hidden in production.

``````{list-table}
:header-rows: 1
:widths: 6 20

* - Syntax
  - Example
* - ````md
    ```{todo}
    todo message here
    ```
    ````
  - ```{todo}
    todo message here
    ```
``````


## Citations

```{note}
Make sure you have a reference bibtex file. And it is included in the `_config.yml`, under `bibtex_bibfiles` section.
```

``````{list-table}
:header-rows: 1
:widths: 20 20 20

* - Syntax
  - Example
  - Result
* - ```md
    {cite}`mybibtexcitation`
    ```
  - ```md
    An example citation {cite}`tani2016`.
    ```
  - An example citation {cite}`tani2016`.
``````

And, at the bottom of the page, include the list of references:

``````md
```{bibliography}
:filter: docname in docnames
```
``````

```{bibliography}
:filter: docname in docnames
```
