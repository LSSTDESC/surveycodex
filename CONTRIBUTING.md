# Contributing to `surveycodex`

We appreciate that you want to contribute to `surveycodex`. Your time is valuable, and your contribution means a lot.

## Important!

By contributing to this project, you agree that the content you contribute may be provided under the project [license](LICENSE), which means that the numbers you provide for a given survey are public or can be made public.

## Getting started

**What does "contributing" mean?**

There are several ways to contribute, namely:

- Feature requests or bug reports through [issues](#issues)
- Add, update or correct information through [pull-requests](#pull-requests)


**Showing support for** `surveycodex`

Don't have time to contribute? No worries, here are some other ways to show your support for `surveycodex`:

- star the [project](https://github.com/LSSTDESC/surveycodex) (creates visibility)
- mention it around

## Issues

To create an issue, go to https://github.com/LSSTDESC/surveycodex/issues/new, provide it with a meaningful title and a description, as well as labels if appropriate.

## Pull-requests

To add, update or correct information, the first step is to setup a development environment for `surveycodex` and then create feature branches for a given [pull-request](https://github.com/LSSTDESC/surveycodex/pulls).

> Note that you will have to [fork the project](https://guides.github.com/activities/forking/) to contribute.

### Getting a development environment (do once)

- Clone the project
    ```sh
    git clone https://github.com/LSSTDESC/surveycodex
    cd surveycodex
    ```
- Setup the virtual environment with the dev tools
    ```sh
    python -m venv venv
    source venv/bin/activate
    python -m pip install -U pip
    ```
- Install `surveycodex` with developer libs
    ```sh
    pip install -e ".[dev]"
    ```
- Install the automated checks and code lint on git commits
    ```sh
    pre-commit install
    ```
- Make sure to regularly run the tests and check code coverage
    ```sh
    pytest --cov
    ```

### Create a fork (do once)

- [Fork the surveycodex project](https://guides.github.com/activities/forking/)
- Add the fork to the list of remote servers
    ```sh
    git remote add fork git@github.com:<your username>/surveycodex.git
    ```

### Code in a feature branch

1. Activate the development environment
    ```sh
    source venv/bin/activate
    ```
2. Create a feature branch (e.g. `featbranch` here)
    ```sh
    git checkout -b featbranch
    ```
3. Commit your code into `featbranch` (sometimes the commit will be rejected because of the `pre-commit` checks, just add the files a second time and commit again).
4. Make sure to integrate the latest changes by regularly incorporating the latest work of the main branch into yours
    ```sh
    git rebase origin/main
    ```
    and solve the conflicts, if any.
5. Push your feature branch to your fork
    ```sh
    git push -u fork featbranch  # the first time to set the target remote
    git push                     # afterwards
    ```
6. Create [the pull-request](https://github.com/LSSTDESC/surveycodex/pulls) and iterate from 3. until it is merged.
