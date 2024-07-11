# README

## Introduction

This project is a codebase health monitoring tool that uses the Greptile API to analyze and report various aspects of a codebase such as security vulnerabilities, bugs, test coverage, technical debt, performance issues, complexity hotspots, code smells, and outdated dependencies. The tool is designed to help developers and teams maintain the health of their codebase by providing insights and actionable data.

## Motivation

Maintaining a healthy codebase is crucial for the long-term success of any software project. This tool aims to automate the process of codebase health monitoring, making it easier for developers to identify and address potential issues before they become major problems. By integrating with the Greptile API and GitHub, this tool provides a comprehensive analysis of the codebase, enabling proactive maintenance and improvements.

## How to Run It

### Prerequisites

- Python 3.6 or higher
- `requests` library
- `python-dotenv` library

### Setup

1. Clone the repository to your local machine.
2. Create a `.env` file in the root directory and add the following environment variables:
    ```
    GREPTILE_API_KEY=your_greptile_api_key
    GITHUB_TOKEN=your_github_token
    ```
3. Install the required libraries:
    ```
    pip install requests python-dotenv
    ```

### Configuration

Ensure a `queries.json` file exists in the root directory. This file contains the query instructions that the script will execute.

### Running the Script

Run the script with the following command:

```
python greptile_client.py
```


## Next Steps

### Add More Queries

Extend the functionality by adding more queries to the `queries.json` file. Examples include:
- **Code Duplication**: Identify duplicated code blocks to improve maintainability. Tools: PMD, SonarQube.
- **Code Coverage by Module**: Get test coverage metrics for individual modules. Tools: Coverage.py, PyTest.
- **Dependency Vulnerabilities**: Check for vulnerabilities in third-party dependencies. Tools: Snyk, OWASP Dependency-Check.


### Improve Output Format

Improving the output format will make the results more user-friendly and easier to analyze. Potential improvements include:

- **HTML Reports**: Use libraries like Jinja2 or ReportLab to generate HTML reports that provide a visual representation of the codebase analysis.
- **CSV Export**: Utilize the pandas library to export the results to a CSV file for easier analysis in spreadsheet applications.
- **Enhanced JSON Output**: Ensure the results are available in a structured JSON format for further processing or integration with other tools.

## Testing

This tool has been tested solely on the Flask repository. Ensure to test it on other repositories to validate its functionality and make necessary adjustments.

### User Interface

Develop a user-friendly interface to visualize the results. This can be a web dashboard or a desktop application that displays the health metrics in an easily understandable format. Tools: React, Flask, Django, Electron.


