import json
import unittest

from src.content_validator import validate_content


class TestContentValidator(unittest.TestCase):

    def test_validate_content_empty_body(self):
        error_message = {"error": "Bad Request", "message": "Empty request"}
        response = validate_content("")

        assert json.loads(response["body"])["error"] == error_message["error"]
        assert response["statusCode"] == 400

    def test_validate_content_invalid_body(self):
        error_message = {"error": "Bad Request", "message": "Empty request"}
        request = {"body": {  }}
        response = validate_content(request)

        assert json.loads(response["body"])["error"] == error_message["error"]
        assert response["statusCode"] == 400

    def test_validate_content_invalid_json(self):
        expected_response = "Invalid json"
        request = {"payload": "this is a test message"}
        response = validate_content(request)

        assert response == expected_response

    def test_validate_content_valid_json(self):
        expected_response = "Valid json"
        request = {"payload": "{\"message\": \"this is a test message\"}"}
        response = validate_content(request)

        assert response == expected_response

if __name__ == '__main__':
    unittest.main()
