import datetime

from sub import config, kse_email


def main(params: dict) -> dict:
    try:
        method: str = params.get("method")
        if method not in ["POST"]:
            raise ValueError({
                "error": "invalid http method",
                "error_code": "auth01",
            })

        body: dict = params.get("body")
        if not body:
            raise ValueError({
                "error": "not params",
                "error_code": "auth02",
            })

        user_id: str = body.get("user_id")
        password: str = body.get("password")

        if not (user_id == config.USER_ID and password == config.PASSWORD):
            kse_email.main({
                "method": "POST",
                "body": {
                    "email": user_id,
                    "phone": "login failed user",
                    "inquiry": "invalid id/password",
                }
            })
            raise ValueError({
                "error": "invalid id/password",
                "error_code": "auth03",
            })

        today = datetime.datetime.today()
        token_base = (today.day * today.month * today.year * today.weekday()) / (today.day + today.month)

        token = f"{config.TOKEN}{token_base}"

        return {
            "status": True,
            "token": token,
        }

    except ValueError as e:
        raise e
