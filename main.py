from fastapi import FastAPI 
from gmail import imap
import disc
import os
from dotenv import load_dotenv
from contextlib import asynccontextmanager
import threading
from summary import summary_func

load_dotenv()
MAIL_USERNAME = os.getenv("MAIL_USERNAME")
if not MAIL_USERNAME:
     print("ERROR: MAIL_USERNAME not found in .env file")
     exit()

MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
if not MAIL_PASSWORD:
     print("ERROR: MAIL_PASSWORD not found in .env file")
     exit()

@asynccontextmanager
async def lifespan(app: FastAPI):

    thread = threading.Thread(target=disc.run_discord, daemon=True)
    thread.start()
    print("Discord bot started.")
    yield
   
    print("App shutting down...")

app = FastAPI(lifespan=lifespan)

@app.get("/")
def test():
    return f"Welcome to MailBell"

@app.get("/mail")
def get_mails():
     summary_mail = summary_func()
     return summary_mail