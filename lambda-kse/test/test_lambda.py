import json

import pytest

import lambda_function
from sub import config

#############################################
# cd test                                   #
# pytest test_lambda.py                     #
#############################################


def set_params(func, method):
    base_params = {
        "method": method,
        "query_parameters": {"func": func, "api_key": config.API_KEY},
        "headers": {},
        "body": {}
    }
    return base_params


def test_base_error_2():
    base_params = set_params("auth", "POST")
    params = base_params["query_parameters"]
    params.update({
        "api_key": "hogehgoe"
    })
    res = lambda_function.main(base_params)
    assert res["body"]["error_code"] == "common01"


def test_base_error_3():
    base_params = set_params("auth", "POST")
    del base_params["query_parameters"]["func"]
    res = lambda_function.main(base_params)
    assert res["body"]["error_code"] == "common02"


def test_base_error_5():
    base_params = set_params("auth", "POST")
    params = base_params["query_parameters"]
    params.update({
        "func": "hogehgoe"
    })
    res = lambda_function.main(base_params)
    assert res["body"]["error_code"] == "common03"


def test_auth_1():
    base_params = set_params("auth", "POST")
    base_params.update({
        "body": {"user_id": "60628565", "password": "Kataguiri616"}
    })
    res = lambda_function.main(base_params)
    assert res["statusCode"] == 200


def test_auth_error_1():
    base_params = set_params("auth", "DELETE")
    base_params.update({
        "body": {"user_id": "60628565", "password": "Kataguiri616"}
    })
    res = lambda_function.main(base_params)
    assert res["body"]["error_code"] == "auth01"


def test_auth_error_2():
    base_params = set_params("auth", "POST")
    res = lambda_function.main(base_params)
    assert res["body"]["error_code"] == "auth02"


def test_auth_error_3():
    base_params = set_params("auth", "POST")
    base_params.update({
        "body": {"user_id": "hoge", "password": "hoge"}
    })
    res = lambda_function.main(base_params)
    assert res["body"]["error_code"] == "auth03"


def test_books_1():
    base_params = set_params("books", "GET")
    res = lambda_function.main(base_params)
    assert res["statusCode"] == 200


def test_books_2():
    base_params = set_params("auth", "POST")
    base_params.update({
        "body": {"user_id": "60628565", "password": "Kataguiri616"}
    })
    res = lambda_function.main(base_params)
    token = res["body"]["token"]

    base_params = set_params("books", "POST")
    base_params.update({
        "body": {
            "books": ["2024-06-08", "2024-06-15"],
            "token": token
        }
    })
    res = lambda_function.main(base_params)
    assert res["statusCode"] == 200


def test_books_error_1():
    base_params = set_params("books", "DELETE")
    res = lambda_function.main(base_params)
    assert res["body"]["error_code"] == "books01"


def test_books_error_2():
    base_params = set_params("books", "POST")
    res = lambda_function.main(base_params)
    assert res["body"]["error_code"] == "books02"


def test_books_error_3():
    base_params = set_params("books", "POST")
    base_params.update({
        "body": {
            "books": ["2024-06-08", "2024-06-15"],
        }
    })
    res = lambda_function.main(base_params)
    assert res["body"]["error_code"] == "books03"


def test_books_error_4():
    base_params = set_params("books", "POST")
    base_params.update({
        "body": {
            "books": ["2024-06-08", "2024-06-15"],
            "token": "hogehoge",
        }
    })
    res = lambda_function.main(base_params)
    assert res["body"]["error_code"] == "books04"


def test_email_1():
    base_params = set_params("email", "POST")
    base_params.update({
        "body": {
            "email": "yuutakatagiri9@gmail.com",
            "phone": "0800000000",
            "inquiry": "hogehoge"
        }
    })
    res = lambda_function.main(base_params)
    assert res["statusCode"] == 200


def test_email_error_1():
    base_params = set_params("email", "DELETE")
    res = lambda_function.main(base_params)
    assert res["body"]["error_code"] == "email01"


def test_email_error_2():
    base_params = set_params("email", "POST")
    res = lambda_function.main(base_params)
    assert res["body"]["error_code"] == "email02"


def test_email_error_3():
    base_params = set_params("email", "POST")
    base_params.update({
        "body": {
            # "email": "yuutakatagiri9@gmail.com",
            "phone": "0800000000",
            "inquiry": "hogehoge"
        }
    })
    res = lambda_function.main(base_params)
    assert res["body"]["error_code"] == "email03"
