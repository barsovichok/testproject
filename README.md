# Test Project

This is a test project designed to demonstrate the integration of Python testing frameworks and Allure for generating comprehensive test reports.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Running Tests](#running-tests)
- [Allure Reporting](#allure-reporting)


## Features

- **Unit Testing**: Comprehensive unit tests using `pytest`.
- **Allure Reporting**: Generate detailed test reports with Allure.
  
## Requirements

- Python 3.12 or higher

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/barsovichok/testproject.git
   cd testproject

2. Install the required Python packages:

  ```bash
  pip install -r requirements.txt

## Running tests

Run command

```bash
pytest --alluredir=allure-results

## Allure Reporting

You can Allure in two ways - see reports in GitHub Pages here or set up allure reporting locally.

For local usage:

1. Install Allure

On MacOs:
 ```bash
brew install allure

or download it from official website - https://allurereport.org/

2. Generate report

```bash
 allure generate allure-results --clean -o allure-report

3. Make HTML-page from it

```bash
allure serve allure-results  


