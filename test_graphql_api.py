import pytest

# Your imports for send_graphql_request and validate_response

@pytest.mark.parametrize("test_data", [
    'test_input_1',
    'test_input_2'
])
def test_api_response(send_graphql_request, validate_response, load_test_data, test_data):
    input_data, expected_output = load_test_data(test_data)
    query = '''
    query Test1($input: TokensInput!) {
      Tokens(input: $input) {
        Token {
          id
          address
          chainId
        }
      }
    }
    '''
    response = send_graphql_request(query, {"input": input_data})
    validate_response(response, expected_output)
