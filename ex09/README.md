# ft_package

A sample Python package created for the 42 School Exercise 09.

## Description

`ft_package` provides a simple function to count how many times an item appears in a list.

## Installation

Build the package with:

```bash
python3 -m build
```

Install the generated package with:

```bash
pip install ./dist/ft_package-0.0.1.tar.gz
```

or:

```bash
pip install ./dist/ft_package-0.0.1-py3-none-any.whl
```

## Usage

```python
from ft_package import count_in_list

print(count_in_list(["toto", "tata", "toto"], "toto"))
# 2

print(count_in_list(["toto", "tata", "toto"], "tutu"))
# 0
```

## License

This project is licensed under the MIT License.
