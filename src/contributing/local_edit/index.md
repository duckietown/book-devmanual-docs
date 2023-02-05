(local-editor-workflow)=
# The right way: Local editor

This section describes the workflow to edit the documentation for one single book.

In a nutshell:

* You *clone* the `book-[name]` repos locally;
* You work on a branch;
* You compile locally and double-check html and pdf outcomes;
* You contribute by opening a pull request.


## Workflow

### GitHub setup

We assume that you have set up a GitHub account with working public keys.

See: [Basic SSH config](+software_reference#github-access).

See: [Key pair creation](+software_reference#howto-create-key-pair).

See: [Adding public key on GitHub](+software_reference#github-access).


### Install Docker

Before you start, make sure that you have [installed Docker](+software_reference#docker).


### Install the Duckietown Shell

Install the Duckietown Shell using [these instructions](https://github.com/duckietown/duckietown-shell).


### Checkout the `book-[name]` repository locally

Check out the book repository locally.

```{attention}
Since the documentation repositories are private, forking on GitHub is disabled.
```


### Create your own branch

Switch to a new branch using the command,

```shell
git checkout -b BRANCH_NAME origin TRACKED_BRANCH
```

where `BRANCH_NAME` is the name you have chosen for your new branch. Branch names should
indicate what the edits held by the branch are about, e.g., `fix-typos`. We also suggest 
prepending the branch name with your username, e.g., `afdaniele-fix-typos`.
Replace `TRACKED_BRANCH` with the branch you want to ultimately merge these changes into, 
for example, `daffy`.


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

Pushing directly to the production branches is not allowed. Somebody has to review your edits before
they can go live. For that you can create a Pull Request through the GitHub website or using your IDE.


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
