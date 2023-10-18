# Development

## Environments

```shell
pipenv install
```

## Necessary Packages

Here are the one-line descriptions for the packages you asked about:

- `pytest`: A Python testing framework that supports various types of software tests.
- `playwright`: A framework for Web Testing and Automation that allows testing Chromium, Firefox and WebKit with a
  single API.
- `pytest-playwright`: A Pytest plugin for Playwright that provides fixtures for automating web browsers (Chromium,
  Firefox, WebKit).
- `pytest-html`: A plugin for pytest that generates a HTML report for test results.
- `pytest-xdist`: A pytest plugin for distributed testing and loop-on-failures testing modes.
- `python-json-logger`: A library that allows standard Python logging to output log data as JSON objects.
- `assertpy`: Assertpy is a simple assertion library for unit testing in Python with a fluent API.

```shell
pipenv install pytest playwright pytest-playwright pytest-html pytest-xdist python-json-logger assertpy
```

## Install Browsers

```shell
playwright install
```

## Linter

- `pre-commit`: A multi-language package manager for pre-commit hooks that manages the installation and execution of any
  hook written in any language before every commit³.

### Install

```shell
pipenv install pre-commit
```

### Check Version

```shell
pre-commit --version
```

### Create Simple Config

```shell
pre-commit sample-config
```

#### Recommended Hooks

```text
https://github.com/pre-commit/pre-commit-hooks
https://github.com/Lucas-C/pre-commit-hooks-safety
https://github.com/PyCQA/bandit
pylint
https://github.com/psf/black
https://github.com/pre-commit/mirrors-mypy
```

### Create pylint Config (It's necessary for pre-commit config)

```shell
pylint --generate-rcfile >.pylintrc
```

### Run (Execute)

```shell
pre-commit run
```

## Screenplay

- `screenpy`: A Python library that provides a composition-based architecture pattern for writing more maintainable
  automated test suites⁵.
- `screenpy_playwright`: An extension to the ScreenPy library that enables interaction with Playwright⁸.

```shell
pipenv install screenpy screenpy_playwright
```
