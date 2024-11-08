import json
import unittest

from src.main import lambda_handler


class TestMain(unittest.TestCase):

    context = {"request_id": "12345", "function_name": "lambda_handler"}

    def test_lambda_handler_empty_request(self):
        error_message = {"error": "Bad Request", "message": "Empty request"}
        response = lambda_handler("", "{}")

        assert json.loads(response["body"])["error"] == error_message["error"]
        assert response["statusCode"] == 400

    def test_lambda_handler_no_auth_token(self):
        error_message = {"error": "Invalid authentication credentials", "message": "Invalid token"}
        request = {
            "headers": {"Authorization": "1234abcd5678efgh"},
            "body": {
                "payload": "{\"this is a test message\"}"
            }
        }
        response = lambda_handler(request, self.context)

        assert json.loads(response["body"])["error"] == error_message["error"]
        assert json.loads(response["body"])["message"] == error_message["message"]
        assert response["statusCode"] == 401

    def test_lambda_handler_bad_request(self):
        error_message = {"error": "Internal Server Error", "message": "Authorization"}
        request = {
            "headers": {"Authentication": "1234abcd5678efgh"},
            "body": {
                "payload": "{\"this is a test message\"}"
            }
        }
        response = lambda_handler(request, self.context)

        assert json.loads(response["body"])["error"] == error_message["error"]
        assert response["statusCode"] == 500

    def test_lambda_handler_invalid_json(self):
        expected_response = {"message": "Operation successful", "data": "Invalid json"}
        request = {
            "headers": {"Authorization": "Bearer 1234abcd5678efgh"},
            "body": {
                "payload": "{\"this is a test message\"}"
            }
        }
        response = lambda_handler(request, self.context)

        assert json.loads(response["body"])["message"] == expected_response["message"]
        assert json.loads(response["body"])["data"] == expected_response["data"]
        assert response["statusCode"] == 200

    def test_lambda_handler_valid_json(self):
        expected_response = {"message": "Operation successful", "data": "Valid json"}
        request = {
                      "headers": {"Authorization": "Bearer 1234abcd5678efgh"},
                      "body": {
                        "payload": "{\"message\": \"this is a test message\"}"
                      }
                    }
        response = lambda_handler(request, self.context)

        assert json.loads(response["body"])["message"] == expected_response["message"]
        assert json.loads(response["body"])["data"] == expected_response["data"]
        assert response["statusCode"] == 200



if __name__ == '__main__':
    unittest.main()
