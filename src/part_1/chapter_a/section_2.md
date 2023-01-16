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

:::{note}
This is a shortlisted version of the [MyST syntax cheat sheet](https://jupyterbook.org/en/stable/reference/cheatsheet.html).
:::

(myst_cheatsheet)=
# MyST syntax cheat sheet

## Headers

``````{list-table}
:header-rows: 1
:widths: 20 15 15

* - Syntax
  - Example
  - Note
* - ```md
    # Heading level 1
    ## Heading level 2
    ### Heading level 3
    #### Heading level 4
    ##### Heading level 5
    ###### Heading level 6
    ```
  - ```md
    # MyST Cheat Sheet
    ```
  - Level 1-6 headings, denoted by number of `#`
``````

## Target headers

``````{list-table}
:header-rows: 1
:widths: 20 15 15

* - Syntax
  - Example
  - Note
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
  - Note
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
  - Note
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
  - Note
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
    [Another page](../../part_2/chapter_c/index.md)
    ```
  - [Another page](../../part_2/chapter_c/index.md)
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

## Admonitions

``````{list-table}
:header-rows: 1
:widths: 10 20 20

* - Syntax
  - Example
  - Result
* - ````md
    ```{note}
    text
    ```
    ````
  - ````md
    ```{note}
    This is an example of a note directive.
    ```
    ````
  - ```{note}
    This is an example of a note directive.
    ```
* - ````md
    ```{warning}
    text
    ```
    ````
  - ````md
    ```{warning}
    This is an example of a warning directive.
    ```
    ````
  - ```{warning}
    This is an example of a warning directive.
    ```
* - ````md
    ```{tip}
    text
    ```
    ````
  - ````md
    ```{tip}
    This is an example of a tip directive.
    ```
    ````
  - ```{tip}
    This is an example of a tip directive.
    ```
* - ````md
    ```{caution}
    text
    ```
    ````
  - ````md
    ```{caution}
    This is an example of a caution directive.
    ```
    ````
  - ```{caution}
    This is an example of a caution directive.
    ```
* - ````md
    ```{attention}
    text
    ```
    ````
  - ````md
    ```{attention}
    This is an example of an attention directive.
    ```
    ````
  - ```{attention}
    This is an example of an attention directive.
    ```
* - ````md
    ```{danger}
    text
    ```
    ````
  - ````md
    ```{danger}
    This is an example of a danger directive.
    ```
    ````
  - ```{danger}
    This is an example of a danger directive.
    ```
* - ````md
    ```{error}
    text
    ```
    ````
  - ````md
    ```{error}
    This is an example of an error directive.
    ```
    ````
  - ```{error}
    This is an example of an error directive.
    ```
* - ````md
    ```{hint}
    text
    ```
    ````
  - ````md
    ```{hint}
    This is an example of a hint directive.
    ```
    ````
  - ```{hint}
    This is an example of a hint directive.
    ```
* - ````md
    ```{important}
    text
    ```
    ````
  - ````md
    ```{important}
    This is an example of an important directive.
    ```
    ````
  - ```{important}
    This is an example of an important directive.
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

## Figures and images

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
    ```{figure} ../../images/image.png
    :width: 30px
    :name: figure-example-2

    Here is my figure caption!
    ```
    ````
  - ```{figure} ../../images/image.png
    :width: 30px
    :name: figure-example-2

    Here is my figure caption!
    ```
* - ````md
    ```{image} ./path/to/figure.jpg
    :name: label
    ```
    ````
  - ````md
    ```{image} ../../images/image.png
    :scale: 10%
    :align: center
    :name: image-example
    ```
    ````
  - ```{image} ../../images/image.png
    :scale: 10%
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
    Ref to [](../../part_2/chapter_b/index.md)
    ```
  - Ref to [](../../part_2/chapter_b/index.md)
* - ```md
    [name](path/to/document)
    ```
  - ```md
    See [here](../../part_2/chapter_b/index.md)
    for more information.
    ```
  - See [here](../../part_2/chapter_b/index.md)
    for more information.
``````

## Footnotes

``````{margin}
<br/><br/><br/><br/>
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

## Citations

```{note}
Make sure you have a reference bibtex file. You can create one by running `touch references.bib`
<!-- or view a {download}`references.bib <../references.bib>` example. -->
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
    This example generates the following
    citation {cite}`perez2011python`.
    ```
  - This example generates the following
    citation {cite}`perez2011python`.
``````

To include a list of citations mentioned in the document, introduce the `bibliography` directive

``````md
```{bibliography}
:filter: docname in docnames
```
``````

<!-- See {doc}`../content/citations` for more information. -->
