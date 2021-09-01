# Contributing to `galcheat`

We appreciate that you want to contribute to `galcheat`. Your time is valuable, and your contribution means a lot.

## Important!

By contributing to this project, you agree that the content you contribute may be provided under the project [license](LICENSE), which means that the numbers you provide for a given survey are public or can be made public.

## Getting started

**What does "contributing" mean?**

There are several ways to contribute, namely:

- Feature requests or bug reports through [issues](#issues)
- Add, update or correct information through [pull-requests](#pull-requests)


**Showing support for** `galcheat`

Don't have time to contribute? No worries, here are some other ways to show your support for `galcheat`:

- star the [project](https://github.com/aboucaud/galcheat) (creates visibility)
- mention it around

## Issues

To create an issue, go to https://github.com/aboucaud/galcheat/issues/new, provide it with a meaningful title and a description, as well as labels if appropriate.

## Pull-requests

To add, update or correct information, the first step is to setup a development environment for `galcheat`

### Getting a development environment (do once)

- Clone the project
    ```sh
    git clone https://github.com/aboucaud/galcheat
    cd galcheat
    ```
- Setup the virtual environment with the dev tools
    ```sh
    python -m venv dev-venv
    source dev-venv/bin/activate
    python -m pip install -r requirements-dev.txt
    ```
- Install the automated checks and code lint on git commits
    ```sh
    pre-commit install
    ```

### Code in a feature branch

1. Don't forget to activate the development environment: `source dev-venv/bin/activate`.
2. Create in a feature branch:
    `git checkout -b <feat-branch>`.
3. Commit your code into `<feat-branch>` (sometimes the commit will be rejected because of the `pre-commit` checks, just add the files a second time).
4. Make sure to integrate the latest changes by regularly incorporating the latest work of the main branch into yours: `git rebase origin/main` and solve the conflicts, if any.
5. Push your feature branch and create a pull-request.
