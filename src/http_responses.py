import json


def __server_error(exception_message: str) -> json:
    # General error handling
    return {
        "statusCode": 500,
        "body": json.dumps({"error": "Internal Server Error", "message": exception_message})
    }

def __error_response(error_message: str) -> json:
    # Return error response for bad request
    return {
        "statusCode": 400,
        "body": json.dumps({"error": "Bad Request", "message": error_message})
    }

def __unauthorized_response() -> json:
    # Return error response for unauthorized request
    return {
        "statusCode": 401,
        "body": json.dumps({"error": "Invalid authentication credentials", "message": "Invalid token"})
    }

def __success_response(result: str) -> json:
    # Return success response
    return {
        "statusCode": 200,
        "body": json.dumps({"message": "Operation successful", "data": result})
    }

