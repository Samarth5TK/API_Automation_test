import requests
import json
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load API URL from configuration file
with open('config.json') as config_file:
    config = json.load(config_file)

# Define the API testing function
def test_status_code():
    url = config["base_url"]
    logging.info(f"Sending GET request to {url}")

    # Send the GET request
    response = requests.get(url)

    # Log response status and headers
    logging.info(f"Received response: {response.status_code}")
    logging.info(f"Response headers: {response.headers}")

    # Validate that the status code is 200
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    print(f"Status Code Verified: {response.status_code}")  # Print status code for clarity

    # Optional: Validate the Content-Type header if needed
    assert 'application/json' in response.headers['Content-Type'], "Expected JSON response"

    logging.info("Test passed. Status code is 200 and Content-Type is JSON.")
