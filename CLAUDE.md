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

- all commits to git should use configuration "Dave Chen" as author and "yexinchen@gmail.com" as email
- this project is going to illustrate many examples of code sample, solution comparison, or company research

## Code Samples
- triggered by requests such as "Illustrate XYZ python"
- key folders such as python, java, rust, typescript will organize code samples across languages
- for example, the python/asyncio folder will be a standalone project that showcases the ability of asyncio
- each of these folder will contain the following:
    - a main entrypoint to the program
        - if it's a python program
            - it needs to be free of any ruff errors
            - it needs to be runnable by uv
            - it needs to have a single file name like main_<topic>.py
                - for example: main_bloomberg_bpipe.py
            - do not create any pyproject.toml files
            - use inline script metadata to specify required dependencies
            - do not mention pip install
            - do not create .python-version
        - if it's Java program
            - it needs to have a single file name like Main<Topic>.java, camelCase convention with Main as prefix
                - for example: MainBloombergBPipe.java
            - it needs a pom.xml to establish dependencies
        - topic should not include language version number such as: gil_314
        - no other source code is needed other than the main entrypoint
    - a README.md that displays the following:
        - important source code with line number
        - output of the program that correlates well with source code line number
        - annotation of output and source code with clear guiding comments referencing source code and output line number
        - state explicitly if the code illustrated requires certain version of language or library

## Solution Comparisons
- triggered by requests such as "Compare Java Dependency Management solutions such as Ant, Gradle and Maven"
- key folder called comparison will contain comparison notes on multiple technologies in a sector
- a file called <sector>.md will be created
- for example, if the objective is to compare Maven, Ant and Gradle for Java dependency management, then create a file called java_dependency_management.md
- This file displays a table comparing various stats for these contending solutions
    - number of stars on Github.com
    - inception date
    - Google trend data
    - Number of contributers
    - staleness of the project
- This file also displays information about each solution, explaining:
    - origin story of the solution
    - key backers for the solution

## Company Research
- triggered by requests such as "Research on a company named XYZ"
- key folder called company will contain research notes on the company
- first step is to find out whether the company is a public or private company
- if it's a public company
    - list a table showing annual financials such as revenue, margin, net income for last 3 years
    - list a table showing quarterly financials such as revenue, margin, net income for last 3 years
    - list out main product and key milestone details for the product offering
    - list out revenue by other dimensions such as geography, demographics
    - list out key annual events that showcase product for this company
- if it's a private company: 
    - list out venture funding information, round, valuation, leading investors in a table
    - list out revenue and financial performance for last 3-5 years
    - list out main product and key milestone details for the product offering
    - list out revenue by other dimensions such as geography, demographics
    - list out annual recurring revenuing for Software-as-service company
    - list out monthly average user for online services
    - list out key annual events that showcase product for this company
- list out main competitors and how each is trying to diffentiate
- save the information into a markdown file in the root folder (ie. Microsoft.md, OpenAI.md, nVidia.md)
    - the markdown file should end with an last update timestamp
- when updating the content, use the last update timestamp to determine content to be retrieved beyond what is already there
