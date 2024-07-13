import datetime
import json
import smtplib
from datetime import datetime, timedelta, timezone
from email.mime.text import MIMEText

from sub import config


def main(params: dict) -> dict:
    try:
        method: str = params.get("method")
        if method not in ["POST"]:
            raise ValueError({
                "error": "invalid http method",
                "error_code": "email01",
            })

        body: dict = params.get("body")
        if not body:
            raise ValueError({
                "error": "not params",
                "error_code": "email02",
            })

        email: str = body.get("email")
        phone: str = body.get("phone")
        inquiry: str = body.get("inquiry")
        if not (email and phone and inquiry):
            raise ValueError({
                "error": "invalid params",
                "error_code": "email03",
            })

        jp_tz = timezone(timedelta(hours=9))
        now_str = datetime.now(jp_tz).strftime("%Y/%m/%d %H:%M:%S")
        subject = f"Inquiry From KSE・Transport HP {now_str}"

        text = inquiry.replace("\n", "<br>")
        html = f'''
        <html>
        <head>
            <style>.text {{border-style: outset; padding: 3%}}</style>
        </head>
        <body>
            <h1><i>{subject}</i></h1>
            <hr><br>
            <b><i>The following message has been received.</i></b>
            <p class="text">
                email: {email}<br>
                phone: {phone}<br><br>
                inquiry: {text}
            </p>
            <br><hr><br>
            <b>
                <i>※ Please do not reply directly to this email.</i>
                <br>
                <i>If you want to contact us, please contact us <a href="mailto:mail@kse-t.jp">mail@kse-t.jp</a></i>
            </b>
        </body>
        </html>
        '''

        smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
        smtpobj.starttls()
        smtpobj.login(config.FROM, config.PW)

        msg = MIMEText(html, "html")
        msg['Subject'] = subject
        msg['To'] = email
        msg['Bcc'] = ",".join(config.TO)

        smtpobj.send_message(msg)
        smtpobj.close()

        return {"status": "success"}

    except ValueError as e:
        raise e
