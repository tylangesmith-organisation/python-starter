
# Python Starter 🐍

This repository aims to implement a few opinions and standards to aid the development of a python project.

## Features

Some things you get right out-of-the-box 📦

- Python Package and Dependency Management with [Poetry](https://python-poetry.org/)
- Code Formatting and Linting with [flake8](https://flake8.pycqa.org/en/latest/) and [black](https://github.com/psf/black)
- Testing with [nox](https://nox.thea.codes/en/stable/)
- Package Versioning and Publishing with [AWS CodeArtifact](https://aws.amazon.com/codeartifact/)
- Support for [VSCode Remote Container](https://code.visualstudio.com/docs/remote/containers) Development Environment

## Getting Started

> For an easier developer experience checkout the [VSCode Remote Container](#vscode-remote-container) section below

As mentioned for development we use [Poetry](https://python-poetry.org/).

To get started with this here are is a list of useful commands to get started with.

```bash
# NOTE: Poetry abstracts away the management of our virtual environments

# Install the dependencies
poetry install

# Run the main entry point of the program
poetry run main

# Run the code formatter
poetry run nox -s black

# Run the code linter
poetry run nox -s lint

# Run the tests
poetry run nox -s test
```

## VSCode Remote Container

> Note you don't have to use VSCode Remote Containers, you can instead use the Docker image directly

If you've never heard of [VSCode Remote Container](https://code.visualstudio.com/docs/remote/containers) before they're great and worth checking out!

The general gist is that VSCode allows you to open up a VSCode workspace within a Docker container. This makes it super simple for new developers to get started. Developers are able to provide a Docker image with all of the dependencies and configurations already setup and installed.

For example in our use case for this project the [Dockerfile](./Dockerfile) image provided installs a few different versions of Python (for matrix testing capabilities), Poetry and nox.
