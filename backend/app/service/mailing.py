import smtplib
import logging
from typing import Any
from email.mime.text import MIMEText

import jinja2
from pydantic import EmailStr

from app import models, utils
from app.config import config


SMTP_SERVER: smtplib.SMTP | None = None
TEMPLATES: jinja2.Environment | None = None


def init_email_service() -> smtplib.SMTP:
    global TEMPLATES
    server = smtplib.SMTP(config.SERVICE_MAIL_HOST, config.SERVICE_MAIL_PORT)
    TEMPLATES = jinja2.Environment(loader=jinja2.FileSystemLoader("app/templates"))
    logging.debug(f"loaded templates {TEMPLATES.list_templates()}")
    server.starttls()
    try:
        server.login(config.SERVICE_MAIL_USER, config.SERVICE_MAIL_PASSWORD)
    except Exception as e:
        logging.error(f"Can't connect to mail server: {e}")
        raise e
    finally:
        logging.info("Connected to mail server")

    return server


def send_mailing(
    to: str, subject: str, template_name: str, template_data: dict
) -> None:
    print("send_mailing")
    global SMTP_SERVER
    global TEMPLATES
    
    print("SMTP_SERVER", SMTP_SERVER)
    print("TEMPLATES", TEMPLATES)
    try:
        if not SMTP_SERVER:
            SMTP_SERVER = init_email_service()
        if not TEMPLATES:
            TEMPLATES = jinja2.Environment(
                loader=jinja2.FileSystemLoader("app/templates")
            )
        print("SMTP_SERVER", SMTP_SERVER)
        print("TEMPLATES", TEMPLATES)
        msg = MIMEText(
            TEMPLATES.get_template(f"{template_name}.html").render(**template_data),
            "html",
        )
        msg["To"] = to
        msg["Subject"] = subject
        SMTP_SERVER.sendmail(config.SERVICE_MAIL_USER, to, msg.as_string())
    except Exception as e:
        logging.error(f"Can't send email: {e}")
        raise e
