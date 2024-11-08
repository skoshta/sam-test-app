import json

from src.content_validator import validate_content
from src.http_responses import (__error_response, __unauthorized_response,
                                __server_error, __success_response)


def lambda_handler(event, context):
    """ Sample lambda function
    1. Validate api request is from approved client by inspecting token
    2. Based on content in request body, perform some action
    3. If message in body is valid json - return True, else return False
    :return: true / false
    """
    try:
        if not event or event == "" or "headers" not in event:
            return __error_response("Empty request")

        # check if valid token present
        token = event.get("headers", "")["Authorization"]
        if not token or not token.startswith("Bearer"):
            # unauthorized access
            return __unauthorized_response()
        else:
            # process this request
            body = event.get("body", "{}")
            result = validate_content(body)
            return __success_response(result)

    except Exception as e:
        # General error handling
        return __server_error(str(e))
