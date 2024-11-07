# API_Automation_test

This project provides a basic setup for API automation testing using Python, designed to verify the status code of a GET request. It uses pytest for test management and requests for handling HTTP requests. The configuration is stored in a JSON file for flexibility and ease of modification.

Requirements
Python 3.6+
Virtual environment (optional but recommended)
`requests` library
`pytest` library

Setup Instructions
Clone the Repository:

`git clone <your-repository-url>`
`cd API Automation Test`

Create a Virtual Environment (optional but recommended):

`python -m venv venv`

Activate the Virtual Environment:
On Windows:
`.\venv\Scripts\activate`
On macOS/Linux:
`source venv/bin/activate`

Install Dependencies:

`pip install requests pytest`

Configure the API URL:
Open config.json and ensure the URL is correctly set.
Example:


`{
  "base_url": "https://reqres.in/api/users?page=2"
}`
Running the Test
To execute the test, run the following command in your terminal:

`pytest -v test_api_status.py`
