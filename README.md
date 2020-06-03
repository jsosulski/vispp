# SPOT in Python

This repository contains the code for SPOT as implemented in python using [mne](https://github.com/mne-tools/mne-python).

## Installation

Setup the `spot_venv` using:

```
make venv
```

## Running scripts

Copy `scripts/local_config.yaml.example` to `scripts/local_config.yaml` and edit the relevant entries in your own file.

Scripts begin with `main_`.

### Running Tests

```
make test
```
