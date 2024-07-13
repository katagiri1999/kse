import datetime
import json

import boto3

from sub import config


def main(params: dict) -> dict:
    try:
        method: str = params.get("method")
        if method not in ["GET", "POST"]:
            raise ValueError({
                "error": "invalid http method",
                "error_code": "books01",
            })

        dynamodb = boto3.resource(service_name="dynamodb", aws_access_key_id=config.AWS_ACCESS_KEY_ID, aws_secret_access_key=config.AWS_SECRET_ACCESS_KEY).Table("KSE-BOOK")
        doc_id = config.ITEM_ID

        if method == "GET":
            records: dict = dynamodb.get_item(Key={"id": doc_id})
            row: dict = records["Item"]
            del row["id"]

            return row

        elif method == "POST":
            body: dict = params.get("body")
            if not body:
                raise ValueError({
                    "error": "no params",
                    "error_code": "books02",
                })

            books: list = body.get("books", [])
            token: str = body.get("token")
            if not token:
                raise ValueError({
                    "error": "no token",
                    "error_code": "books03",
                })

            today = datetime.datetime.today()
            token_base = (today.day * today.month * today.year * today.weekday()) / (today.day + today.month)

            if (token != f"{config.TOKEN}{token_base}"):
                raise ValueError({
                    "error": "invalid token",
                    "error_code": "books04",
                })

            dynamodb.update_item(
                Key={"id": doc_id},
                UpdateExpression='set #books = :books',
                ExpressionAttributeNames={'#books': 'books'},
                ExpressionAttributeValues={':books': books}
            )

            return {"status": "success"}

    except ValueError as e:
        raise e
