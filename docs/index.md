# Welcome to `galcheat`

`galcheat` is a tiny package containing useful parameters from main galaxy surveys (**with units**).

The goal of this project is to provide a Python library with minimal dependencies that centralises galaxy survey properties with adequate reference. Such information tends to be scattered in many places or is often copy/pasted without all of the relevant information like units or sources.

## Command line interface

Pretty print the available surveys and associated filters in the terminal

```bash
galcheat
```

### Options

- **`-s <survey>`**: print information for a given survey
- **`--refs`**: print the source for each parameter
- **`--rich`**: use pretty printing for the terminal (needs the `rich` library installed)
- **`-h, --help`**: get help

### Examples

```sh
galcheat -s LSST         # LSST info
galcheat --refs          # all surveys info with refs
galcheat --refs -s HSC   # HSC info with refs
galcheat -s LSST --rich  # pretty print rich terminal output for LSST survey info
```

## Installation

```sh
python -m pip install -U galcheat
```

## Optional installation

### Scripts

To run the Python scripts from the `script` folder, use the extra install

```sh
python -m pip install -U galcheat[scripts]
```

### Developers

The developer tools needed to perform tests and linting and compile the docs locally can be installed with

```sh
python -m pip install -U galcheat[dev]
```

### Rich display (new in v1.1)

For a better terminal experience, install the `rich` library and use it together with the `--rich` option from `galcheat`

```sh
python -m pip install rich
```
