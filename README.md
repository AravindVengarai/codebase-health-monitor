# README

## Introduction

This project is a codebase health monitoring tool that uses the Greptile API to analyze and report various aspects of a codebase such as security vulnerabilities, bugs, test coverage, technical debt, performance issues, complexity hotspots, code smells, and outdated dependencies. The tool is designed to help developers and teams maintain the health of their codebase by providing insights and actionable data.

## Motivation

Maintaining a healthy codebase is crucial for the long-term success of any software project. This tool aims to automate the process of codebase health monitoring, making it easier for developers to identify and address potential issues before they become major problems. By integrating with the Greptile API and GitHub, this tool provides a comprehensive analysis of the codebase, enabling proactive maintenance and improvements.

## What It Is

This tool is a Python script that:
1. Loads environment variables for API authentication.
2. Defines constants and headers for making API requests.
3. Loads a set of predefined queries from a JSON file.
4. Ensures the specified GitHub repository is indexed by the Greptile API.
5. Executes the queries against the codebase.
6. Prints the results to the console.

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

python greptile_client.py


## Next Steps

### Improve Error Handling

Enhance the error handling mechanism to provide more detailed and specific error messages. This can be achieved by categorizing errors and using custom exceptions to handle different scenarios.

### Add More Queries

Extend the functionality by adding more queries to the `queries.json` file. Examples include:
- **Code Duplication**: Identify duplicated code blocks to improve maintainability. Tools: PMD, SonarQube.
- **Code Coverage by Module**: Get test coverage metrics for individual modules. Tools: Coverage.py, PyTest.
- **Dependency Vulnerabilities**: Check for vulnerabilities in third-party dependencies. Tools: Snyk, OWASP Dependency-Check.

### Integrate with CI/CD

Integrate this tool into a CI/CD pipeline to automate codebase health monitoring. This ensures that every change in the codebase is analyzed, and potential issues are reported immediately. Tools: Jenkins, GitHub Actions, GitLab CI.

### Enhance Documentation

Improve the documentation to cover more aspects of the tool, including detailed setup instructions, usage examples, and explanations of the different queries and their importance.

### User Interface

Develop a user-friendly interface to visualize the results. This can be a web dashboard or a desktop application that displays the health metrics in an easily understandable format. Tools: React, Flask, Django, Electron.

These steps aim to enhance the functionality and usability of the tool while maintaining its readability and simplicity.
