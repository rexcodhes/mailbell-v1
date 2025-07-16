from imap_tools.mailbox import MailBox
import os
from dotenv import load_dotenv

load_dotenv()
MAIL_USERNAME = os.getenv("MAIL_USERNAME")
if not MAIL_USERNAME:
    print("ERROR: MAIL_USERNAME not found in .env file")
    exit()

MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
if not MAIL_PASSWORD:
    print("ERROR: MAIL_PASSWORD not found in .env file")
    exit()

mails = []

def imap(MAIL_USERNAME, MAIL_PASSWORD):
    with MailBox("imap.gmail.com").login(MAIL_USERNAME, MAIL_PASSWORD, "Inbox") as mb:
        global mails
        mails = []
        for msg in mb.fetch(limit=5, reverse=True, mark_seen=True):
            response = [
                f"Subject: {msg.subject}",
                f"Date: {msg.date}",
                f"Text: {msg.text}"
            ]
            mails.append(response)
        return mails