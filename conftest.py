import pytest
import requests
import configparser
import json

# Read configuration from config.ini
config = configparser.ConfigParser()
config.read('config.ini')

# Fixture to send a GraphQL request
@pytest.fixture(scope="function")
def send_graphql_request():
    def _send_graphql_request(query, variables):
        endpoint_url = config.get('API', 'endpoint_url')
        headers = {
            "Content-Type": "application/json"
        }
        data = {
            "query": query,
            "variables": variables
        }
        response = requests.post(endpoint_url, json=data, headers=headers)
        return response.json()
    return _send_graphql_request

# Fixture to validate response against expected fields
@pytest.fixture(scope="function")
def validate_response():
    def _validate_response(response, expected_fields):
        data = response.get("data")
        if data:
            for key in data:
                assert key in expected_fields, f"Unexpected field '{key}' in the response"
                for field in data[key]:
                    assert all(key in field for key in expected_fields[key]), f"Missing field in {key} object"
        else:
            assert "errors" in response, "GraphQL errors not found in response"
    return _validate_response

# Fixture to load input and expected output from config.ini
@pytest.fixture(scope="function")
def load_test_data():
    def _load_test_data(test_case):
        input_data = config.get('TestData', test_case)
        expected_output = config.get('TestData', f'expected_output_{test_case.split("_")[-1]}')
        return json.loads(input_data), json.loads(expected_output)
    return _load_test_data
