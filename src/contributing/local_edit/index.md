(duckumentation-workflow)=
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

### Fork the `docs-![book]` repo on the Github site

Fork one of the `docs-![book]` repos on the Github site ([](#fork-duckuments)).

This will create a new repo on your account that is linked to the original one.

<figure id="fork-duckuments">
 <img src="fork-duckuments.png" style='width: 80%'/>
</figure>

<!--

TODO: re-make image

-->

### Checkout your fork locally

Check out the forked repository as you would do normally.

### Initialize your folder

Go into the folder:

    $ cd docs-![book]


When compiling a book for the first time, you need to run:

    $ git submodule init

And:

    $ git submodule update

### Do your edits

Do your edits on your local copy. The source files are in the directory `book/![book]`. The file and folder names start with numbers, these are used to determine the order that things show up in output.

### Compile

Compile using the `docs` commands in the Duckietown Shell:

    $ dts docs build

Re-compile from scratch using:

    $ dts docs clean
    $ dts docs build

If there are errors you should open `duckuments-dist/errors.html` and look at them and fix them.

### Look at the local copy

Open the file `index.html` and navigate to whichever pages you have changed to make sure that they look the way want them to.

### Commit and push

Commit and push as you would do normally.

### Make a pull request

Create a pull request to the original repository.

#### Option 1: Use the Github website

Github offers a nice interface to create a pull request.

TODO for volunteer: add image of pull request

#### Option 2: Use the command-line program `hub`

You can create a pull request from the command-line using [`hub`](+software_reference#hub):

```
$ hub pull-request
```

See: [](+software_reference#hub)

## Using CircleCI {#duckumentation-workflow-circle}

Circle CI makes it easier to check whether there are problems to be fixed.

### Sign up on Circle

Sign up on the Circle CI service, at the link [circleci.com](http://circleci.com).

### Activate your build on Circle

Activate the building at the link:

```
https://circleci.com/setup-project/gh/![username]/duckuments
```

where `![username]` is your Github username.

Click "start building".


####  Make sure everything compiles on Circle

Go to the URL:

```
https://circleci.com/gh/![username]/duckuments
```

to see the status of your build.

You can also preview the results by clicking the "artifacts" tab and selecting `index.html` from the list.

<figure id="ci-artifacts">
 <img src='ci-artifacts.png' style='width:90%'/>
</figure>