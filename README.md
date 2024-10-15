# Test Project

This is a test project designed to demonstrate the integration of Python testing frameworks and Allure for generating comprehensive test reports.


## Features

- **API Testing**: Comprehensive unit tests using `pytest`.
- **Allure Reporting**: Generate detailed test reports with Allure.
  
## Requirements

- Python 3.12 or higher

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/barsovichok/testproject.git
   cd testproject

2. Install the required Python packages:

  
  ```pip install -r requirements.txt```

## Running tests


```pytest --alluredir=allure-results```


## Allure Reporting

You can Allure in two ways - see reports in GitHub Pages here https://barsovichok.github.io/testproject/ or set up allure reporting locally.


For local usage:

1. Install Allure

On MacOs:

```brew install allure```

or download it from official website - https://allurereport.org/

2. Generate report


 ```allure generate allure-results --clean -o allure-report```

3. Make HTML-page from it


```allure serve allure-results```


