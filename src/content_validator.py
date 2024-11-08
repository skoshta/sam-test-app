import json

from src.http_responses import __error_response, __success_response


def validate_content(body: json) -> str:
    if not body or "payload" not in body:
        return __error_response("Missing content")

    payload = body["payload"]
    try:
        json.loads(payload)
        return "Valid json"
    except ValueError:
        return "Invalid json"

