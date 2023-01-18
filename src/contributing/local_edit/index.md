(local-editor-workflow)=
# The right way: Local editor 

```{tableofcontents}
```

This section describes the workflow to edit the documentation for one single book.

In a nutshell:

* You *fork* the repos to your Github account.
* You compile locally using a Docker container (no installation necessary).
* You contribute by opening a pull request.

## Workflow

### Github setup

We assume that you have setup a Github account with working public keys.

See: [Basic SSH config](+software_reference#github-access).

See: [Key pair creation](+software_reference#howto-create-key-pair).

See: [Adding public key on Github](+software_reference#github-access).

### Install Docker

Before you start, make sure that you have [installed Docker](+software_reference#docker).

### Install the Duckieton Shell

Install the Duckietown Shell using [these instructions](https://github.com/duckietown/duckietown-shell).

### Fork the `book-[name]` repository on GitHub

Navigate to the book repository page on GitHub, and click on the {bdg-dark-line}`Fork` button at
the top-right corner of the page.

This will create a new repository on your account that is linked to the original one.


### Checkout your fork locally

Check out the forked repository locally.


### Do your edits

Do your edits on your local copy. 
The source files are in the directory `src/`. 

Images are stored in the directory `src/_images`, while `CSS` and `JS` files can be dropped inside the
directory `src/_static` and will be automatically loaded.


### Compile HTML

Compile using the `dts docs` commands in the Duckietown Shell:

    dts docs build

Clean up artifacts and build cache with the command,

    dts docs clean


#### View the HTML

Once built, the book will be exported as HTML inside the directory `html/`.
Open the file `html/index.html` to start. Make sure that your changes look the way you want them to.


### Compile PDF

Compile the book into a PDF file using the command,

    dts docs build --pdf


#### View the PDF

Once built, the book will be exported as PDF inside the directory `pdf/`.
Open the file `pdf/book.pdf` to start. Make sure that your changes look the way you want them to.


### Commit and push

Commit and push as you would do normally.


### Make a pull request

Create a pull request to the original repository.


### Publish artifacts directly

While it is recommended to use Continuous Integration (CI) systems (e.g., Jenkins, CircleCI) to perform
automatic builds and deployments of the documentation, you can decide to push your local artifacts to the
corresponding HTTP server.
You can do so by running the following command,

    dts docs publish [DNS]

where `[DNS]` is the hostname of the documentation website to push the artifacts to, 
e.g., `docs.duckietown.com`.
