# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Package Management and Tooling

For Python code samples:
use [uv](https://docs.astral.sh/uv/) for all Python tooling and dependency management.
use ruff for all Python linting needs.

- **Run Python code**: `uv run python <script.py>` (NOT `python` directly - this ensures the environment is set up correctly)
- **Linting/formatting**: `uv run ruff check` and `uv run ruff format`

For Java code samples:
use Maven for Java dependency management.

## Project Structure

- this project is going to illustrate many examples of code sample
- key folders such as python, java, rust, typescript will organize code samples across languages
- for example, the python/asyncio folder will be a standalone project that showcases the ability of asyncio
- each of these folder will contain the following:
    - a main entrypoint to the program
        - if it's a python program
            - it needs to be free of any ruff errors
            - it needs to be runnable by uv
            - it needs to have a file name like main_<topic>.py
                - for example: main_bloomberg_bpipe.py
            - do not create any pyproject.toml files
            - use inline script metadata to specify required dependencies
            - do not mention pip install
            - do not create .python-version
        - if it's Java program
            - it needs to have a file name like Main<Topic>.java
                - for example: MainBloombergBPipe.java
        - topic should not include language version number such as: gil_314
    - a readme.md that displays the following:
        - important source code with line number
        - output of the program that correlates well with source code line number
        - annotation of output and source code with clear guiding comments referencing source code and output line number
        - state explicitly if the code illustrated requires certain version of language or library
