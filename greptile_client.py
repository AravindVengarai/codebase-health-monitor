import os
import time
import requests
import json
import logging
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

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def load_queries(filename="queries.json"):
    """Load queries from a JSON file."""
    try:
        with open(filename, 'r') as file:
            return json.load(file)['queries']
    except Exception as e:
        logger.error(f"Failed to load queries from {filename}: {e}")
        raise

def make_request(url, method='GET', data=None):
    """Make an HTTP request and return the response."""
    try:
        if method == 'POST':
            response = requests.post(url, json=data, headers=headers)
        else:
            response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"HTTP request failed: {e}")
        raise

def index_repository():
    """Index the repository."""
    url = f'{BASE_URL}/repositories'
    return make_request(url, method='POST', data=REPO_DETAILS)

def check_indexing_status():
    """Check the indexing status of the repository."""
    url = f'{BASE_URL}/repositories/{REPO_ID}'
    return make_request(url)

def query_codebase(question):
    """Query the codebase."""
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
    return make_request(url, method='POST', data=data)

def ensure_indexed():
    """Ensure the repository is indexed before querying."""
    status = check_indexing_status()
    if status.get('status') != 'completed':
        logger.info("Indexing repository...")
        index_repository()
        while True:
            time.sleep(60)  # Wait before checking again
            status = check_indexing_status()
            logger.info(f"Indexing status: {status.get('status')}")
            if status.get('status') == 'completed':
                break
    logger.info("Repository indexed and ready for querying.")

def extract_message(response):
    """Extract message from the response."""
    try:
        return response.get('message', "No message found in response.")
    except (KeyError, json.JSONDecodeError, IndexError) as e:
        return f"Error extracting message: {str(e)}"

def get_codebase_data(queries):
    """Get codebase data based on the provided queries."""
    ensure_indexed()

    results = {}
    for key, value in queries.items():
        logger.info(f"Querying {key.replace('_', ' ')} data...")
        try:
            query_result = query_codebase(value['description'])
            result_message = extract_message(query_result)
            results[key] = result_message
            logger.info(f"{key.replace('_', ' ').capitalize()} query result: {result_message}")
        except Exception as e:
            logger.error(f"Failed to query {key.replace('_', ' ')}: {e}")
            results[key] = str(e)
    
    # Print the results
    for key, result in results.items():
        print(f"{key.replace('_', ' ').capitalize()} query result: {result}")

def main(queries_file="queries.json"):
    """Main function to get codebase data and print to console."""
    queries = load_queries(queries_file)
    get_codebase_data(queries)

if __name__ == "__main__":
    main()
