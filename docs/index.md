# Welcome to `surveycodex`

`surveycodex` is a tiny package containing useful parameters from main galaxy surveys (**with units**).

The goal of this project is to provide a Python library with minimal dependencies that centralises galaxy survey properties with adequate reference. Such information tends to be scattered in many places or is often copy/pasted without all of the relevant information like units or sources.

## Command line interface

Pretty print the available surveys and associated filters in the terminal

```bash
surveycodex
```

### Options

- **`-s <survey>`**: print information for a given survey
- **`--refs`**: print the source for each parameter
- **`--rich`**: use pretty printing for the terminal (needs the `rich` library installed)
- **`-h, --help`**: get help

### Examples

```sh
surveycodex -s LSST         # LSST info
surveycodex --refs          # all surveys info with refs
surveycodex --refs -s HSC   # HSC info with refs
surveycodex -s LSST --rich  # pretty print rich terminal output for LSST survey info
```

## Installation

```sh
python -m pip install -U surveycodex
```

## Optional installation

### Scripts

To run the Python scripts from the `script` folder, use the extra install

```sh
python -m pip install -U surveycodex[scripts]
```

### Developers

The developer tools needed to perform tests and linting and compile the docs locally can be installed with

```sh
python -m pip install -U surveycodex[dev]
```

### Rich display (new in v1.1)

For a better terminal experience, install the `rich` library and use it together with the `--rich` option from `surveycodex`

```sh
python -m pip install rich
```
