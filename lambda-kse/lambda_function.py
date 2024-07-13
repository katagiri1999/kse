import json
import traceback

from sub import config, kse_auth, kse_books, kse_email


def request_handler(event: dict) -> dict:
    try:
        ret = {
            "method": event["requestContext"]["http"]["method"],
            "headers": event["headers"],
            "query_parameters": {},
            "body": {},
        }

        if event.get("queryStringParameters"):
            ret.update({"query_parameters": event["queryStringParameters"]})
        if event.get("body"):
            ret.update({"body": json.loads(event["body"])})

        return ret

    except Exception as e:
        raise e


def main(params: dict) -> dict:
    try:
        print("request: " + json.dumps(params))

        query_parameters: dict = params.get("query_parameters")
        api_key: str = query_parameters.get("api_key")
        if api_key != config.API_KEY:
            raise ValueError({
                "error": "invalid api key",
                "error_code": "common01",
            })

        func_name: str = query_parameters.get("func")
        if not func_name:
            raise ValueError({
                "error": "no func",
                "error_code": "common02",
            })

        if func_name == "auth":
            res = kse_auth.main(params)
        elif func_name == "email":
            res = kse_email.main(params)
        elif func_name == "books":
            res = kse_books.main(params)
        else:
            raise ValueError({
                "error": "invalid func",
                "error_code": "common03",
            })

        res = {
            "statusCode": 200,
            "headers": {"Content-type": "application/json"},
            "body": res,
        }

        print("response: " + json.dumps(res))
        return res

    except ValueError as e:
        res = {
            "statusCode": 400,
            "headers": {"Content-type": "application/json"},
            "body": e.args[0],
        }
        print("response: " + json.dumps(res))
        return res

    except Exception as e:
        res = {
            "statusCode": 500,
            "headers": {"Content-type": "application/json"},
            "body": {"status": traceback.format_exc()},
        }
        print("response: " + json.dumps(res))
        return res


def lambda_handler(event: dict, context) -> dict:
    params = request_handler(event)
    res = main(params)
    return res
