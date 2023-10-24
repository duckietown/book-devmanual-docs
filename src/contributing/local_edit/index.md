(local-editor-workflow)=
# The right way: Local editor 

This section describes the workflow to edit the documentation for one single book.

In a nutshell:

* *Fork* the repos to your GitHub account.
* Compile locally using a Docker container (no installation necessary).
* Contribute by opening a pull request.


## Workflow

### GitHub setup

We assume that you have set up a GitHub account with working public keys.

See: [GitHub SSH config](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent).

### Install Docker

Before you start, make sure that you have [installed Docker](book-opmanual-duckiebot:laptop-setup-docker).


### Install the Duckietown Shell

Install the Duckietown Shell using [these instructions](book-opmanual-duckiebot:laptop-setup-shell).

### Fork the `book-[name]` repository on GitHub

Navigate to the book repository page on GitHub, and click on the {bdg-dark-line}`Fork` button in
the top-right corner of the page.

This will create a new repository on your account that is linked to the original one.


### Checkout your fork locally

Check out the forked repository locally.


### Do your edits

Do your edits on your local copy of the repository.
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

```{attention}
You need to be part of the [`Developers - Docs`](https://github.com/orgs/duckietown/teams/developers-docs)
team on GitHub to be able to push changes to the documentation repositories. Ask your supervisor if you
don't have access.
```


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

```{note}
This is only allowed on staging servers, e.g., `staging-docs.duckietown.com`. Only Jenkins can publish
to production.
```
