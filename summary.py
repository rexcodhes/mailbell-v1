import os
import pathlib
from dotenv import load_dotenv
import google.generativeai as genai
import gmail
env_path = pathlib.Path(__file__).resolve().parent / ".env"

load_dotenv(dotenv_path=env_path)
MAIL_USERNAME = os.getenv("MAIL_USERNAME")
if not MAIL_USERNAME:
    print("ERROR: MAIL_USERNAME not found in .env file")
    exit()

MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
if not MAIL_PASSWORD:
    print("ERROR: MAIL_PASSWORD not found in .env file")
    exit()
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

def summary_func():
    print("Fetching mails")
    fetch = gmail.imap(MAIL_USERNAME, MAIL_PASSWORD)
    model = genai.GenerativeModel("gemini-2.0-flash")
    prompt = ("You are an intelligent email summarization bot. Your task is to provide a concise, point-wise summary for each email provided."
    " For each summary, clearly state the subject of the email first. Crucially, filter out and *do not* summarize any emails identified as promotional or spam. Present the summaries as a numbered list." + f"{fetch}")
    print("Generating summary")
    response = model.generate_content(prompt)
    print("Finished summarising")
    return response.text.strip()