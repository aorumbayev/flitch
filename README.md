<p align="center">
    <img width=60% src="https://github.com/aorumbayev/flitch/blob/master/misc/logo-min.png?raw=true" border="0" />
</p>

<p align="center">
 <a href="https://opensource.org/licenses/MIT"><img src="https://github.com/aorumbayev/flitch/workflows/CI/badge.svg?branch=dev"></a>
 <a href="https://badge.fury.io/py/flitch"><img src="https://badge.fury.io/py/flitch.svg" alt="PyPI version" height="18"></a>
 <a href="https://aorumbayev.github.io/flitch/"><img src="https://img.shields.io/badge/Documentation-pdoc-Blue.svg" alt="pdoc" /></a>
 <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/license-MIT-blue.svg"></a>
</p>

<p align="center">
  Flitch is a collection of simple utilities for splitting text files
</p>

## Table of contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Examples](#examples)
- [Testing](#contributing)

## Prerequisites

The following set of technologies is required to be installed:

- [Python 3.6](https://www.python.org/downloads/release/python-360/) and higher
- [Poetry](https://python-poetry.org) a python dependency manager

## Installation

```bash
poetry install
```

## Examples

The following section demonstrates usage of various file splitting functions available.

### Splitting text file into `n` parts

Example below demonstrated a sample invocation of parts splitter.

```python
import flitch

flitch.split_into_parts("{input_file}", "{output_folder}", 10)
```

For more details refer to [Documentation]()

### Testing

The following assumes that all dependencies are installed and virtual environment is activated via `poetry`.

```bash
pytest
```
