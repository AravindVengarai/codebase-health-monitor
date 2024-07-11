import os
import time
import requests
import json
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Constants
GREPTILE_API_KEY = os.getenv('GREPTILE_API_KEY')
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
BASE_URL = 'https://api.greptile.com/v2'
REPO_ID = 'github%3Amain%3AAravindVengarai%2Fflask'
REPO_DETAILS = {
    "remote": "github",
    "repository": "AravindVengarai/flask",
    "branch": "main"
}

# Headers for requests
headers = {
    'Authorization': f'Bearer {GREPTILE_API_KEY}',
    'X-Github-Token': GITHUB_TOKEN,
    'Content-Type': 'application/json'
}

# Function to index the repository
def index_repository():
    url = f'{BASE_URL}/repositories'
    response = requests.post(url, json=REPO_DETAILS, headers=headers)
    response.raise_for_status()
    return response.json()

# Function to check the indexing status
def check_indexing_status():
    url = f'{BASE_URL}/repositories/{REPO_ID}'
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

# Function to query the codebase
def query_codebase(question):
    url = f'{BASE_URL}/query'
    data = {
        "messages": [
            {
                "id": "health-query",
                "content": question,
                "role": "user"
            }
        ],
        "repositories": [
            REPO_DETAILS
        ],
        "sessionId": "health-monitor-session"
    }
    response = requests.post(url, json=data, headers=headers)
    response.raise_for_status()
    return response.json()

# Function to ensure the repository is indexed
def ensure_indexed():
    status = check_indexing_status()
    if status.get('status') != 'completed':
        print("Indexing repository...")
        index_repository()
        while True:
            time.sleep(60)  # Wait before checking again
            status = check_indexing_status()
            print(f"Indexing status: {status.get('status')}")
            if status.get('status') == 'completed':
                break
    print("Repository indexed and ready for querying.")

# Function to extract message from the response
def extract_message(response):
    try:
        return response.get('message', "No message found in response.")
    except (KeyError, json.JSONDecodeError, IndexError) as e:
        return f"Error extracting message: {str(e)}"

# Function to get codebase data
def get_codebase_data():
    ensure_indexed()

    print("Querying codebase data...")

    # Query outdated dependencies
    outdated_dependencies_data = query_codebase(
        "Count the number of outdated dependencies in this codebase. "
        "Provide the count as a single integer. "
        "Format your response as JSON with a single key 'outdated_dependencies'."
    )
    print(f"Outdated dependencies query result: {extract_message(outdated_dependencies_data)}")
    print("Completed query for outdated dependencies.")

    # Query security vulnerabilities
    security_vulnerabilities_data = query_codebase(
        "List any security vulnerabilities found in the codebase, including the specific files and lines where they occur. "
        "Provide the details as a JSON object with keys 'vulnerabilities', 'file', 'line', and 'count'."
    )
    print(f"Security vulnerabilities query result: {extract_message(security_vulnerabilities_data)}")
    print("Completed query for security vulnerabilities.")

    # Query code smells
    code_smells_data = query_codebase(
        "Identify any potential code smells in the codebase, including specific files, lines, and a level of badness where they occur. "
        "Provide the details as a JSON object with keys 'code_smells' and 'count'."
    )
    print(f"Code smells query result: {extract_message(code_smells_data)}")
    print("Completed query for code smells.")

    # Query test coverage
    test_coverage_data = query_codebase(
        "What percentage of the codebase is covered by tests? "
        "Provide the test coverage as a single number with two decimal places. "
        "Format your response as JSON with a single key 'test_coverage'."
    )
    print(f"Test coverage query result: {extract_message(test_coverage_data)}")
    print("Completed query for test coverage.")

    # Query documentation coverage
    documentation_coverage_data = query_codebase(
        "What percentage of the codebase is documented? "
        "Provide the documentation coverage as a single number with two decimal places. "
        "Format your response as JSON with a single key 'documentation_coverage'."
    )
    print(f"Documentation coverage query result: {extract_message(documentation_coverage_data)}")
    print("Completed query for documentation coverage.")

    # Query bugs
    bugs_data = query_codebase(
        "Identify any bugs in the codebase. "
        "Provide the details as a JSON object with keys 'bugs' and 'count'."
    )
    print(f"Bugs query result: {extract_message(bugs_data)}")
    print("Completed query for bugs.")

    # Query technical debt
    technical_debt_data = query_codebase(
        "Analyze the technical debt in the codebase. "
        "Provide the technical debt as a single number with two decimal places. "
        "Format your response as JSON with a single key 'technical_debt'."
    )
    print(f"Technical debt query result: {extract_message(technical_debt_data)}")
    print("Completed query for technical debt.")

    # Query complexity hotspots
    complexity_hotspots_data = query_codebase(
        "Identify any complexity hotspots in the codebase. "
        "Provide the details as a JSON object with keys 'complexity_hotspots' and 'count'."
    )
    print(f"Complexity hotspots query result: {extract_message(complexity_hotspots_data)}")
    print("Completed query for complexity hotspots.")

def main():
    get_codebase_data()

if __name__ == "__main__":
    main()
