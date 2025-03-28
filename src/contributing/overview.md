```{seo}
:description: Learn about the general layout of Duckietown documentation and how to contribute.  
:keywords: duckietown, documentation, overview, markdown, html, sphynx
```

(duckumentation-intro)=
# Overview

(where_documentation_is)=
## Where the documentation is

The documentation is broken down into a collection of books, with each book contained in a separate repository called `book-[name]`:

For example:

* [`book-devmanual-docs`](https://github.com/duckietown/book-devmanual-docs) (this book)
* [`book-opmanual-duckiebot`](https://github.com/duckietown/book-opmanual-duckiebot)

(documentation_format)=
## Documentation format

The documentation is written as a series of small files in Markedly Structured Text (MyST), a Markdown format inspired by Sphinx and reStructuredText (RST).

It is then processed by a series of scripts to create publication-quality PDF and an online HTML version.

You can find all these artifacts produced at the site [`https://docs.duckietown.com`](https://docs.duckietown.com).

(documentation_branches_and_more)=
## Documentation branches

Each book repository has several branches. In particular, the `daffy` branch includes documentation related to the `daffy` Duckietown software distribution. The `ente` branch describes the `ente` version of Duckietown software distribution, and it is substantially different from the older `daffy` version. 

`Daffy` documentation can be found at [`https://docs.duckietown.com/daffy`](https://docs.duckietown.com/daffy), and the respective content available on the [Duckietown GitHub](https://github.com/duckietown), in repositories named `docs-[book name]`, e.g., the [Old Duckiebot operation manual](https://github.com/duckietown/docs-opmanual_duckiebot). 

`Ente` documentation can be found at [`https://docs.duckietown.com/ente`](https://docs.duckietown.com/ente).

### Deprecated documentation system

The older, now deprecated, Duckietown documentation system is available at: [https://docs-old.duckietown.org/daffy/](https://docs-old.duckietown.org/daffy/). 
