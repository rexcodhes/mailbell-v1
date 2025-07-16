
# 📬 MailBell — Your Smart Email Summarizer + Discord Bot

MailBell is a Python-based application that combines **FastAPI**, **Discord bot integration**, and **Google Gemini AI** to fetch your recent Gmail messages and deliver AI-generated, point-wise summaries—directly via API or Discord.

---

## 🚀 Features

- ✉️ Fetches the 5 most recent Gmail emails using IMAP
- 🧠 Summarizes emails using **Gemini 2.0 Flash** model
- 🔒 Filters out spam/promotional content intelligently
- 🤖 Discord Bot with commands to trigger email summaries
- 🌐 FastAPI backend to serve summaries via REST endpoint

---

## 🗂️ Project Structure

```
📦 MailBell
├── main.py              # FastAPI application
├── disc.py              # Discord bot integration
├── gmail.py             # Gmail fetching via IMAP
├── summary.py           # Gemini-powered summarization
├── requirements.txt     # Python dependencies
└── .env                 # Environment variables (not included)
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/mailbell.git
cd mailbell
```

### 2. Create a `.env` File
Create a `.env` file in the root directory with the following variables:

```env
MAIL_USERNAME=your_gmail_address
MAIL_PASSWORD=your_app_password
GEMINI_API_KEY=your_gemini_api_key
DISCORD_TOKEN=your_discord_bot_token
base_url=http://localhost:8000
```

> **Note:** Use a Gmail [App Password](https://support.google.com/mail/answer/185833) for `MAIL_PASSWORD`.

### 3. Install Dependencies
It’s recommended to use a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 4. Run the Application
```bash
uvicorn main:app --reload
```

---

## 🤖 Discord Commands

| Command        | Description                          |
|----------------|--------------------------------------|
| `!email`       | Sends summarized emails via DM       |

---

## 🧠 AI Summary Example

When `GET /mail` or `!email` is triggered, Gemini AI provides a clean summary like:

```
1. 📌 Subject: Meeting Tomorrow
   - Reminder for team sync at 10 AM
   - Agenda includes roadmap updates and Q&A

2. 📌 Subject: Invoice #345
   - Payment confirmation received
   - No further action required
```

---

## 🛡️ Security & Privacy

- Your email credentials are stored in a local `.env` file and **never exposed** in code.
- Uses Google’s Gemini AI to summarize email content **locally via API**—no third-party email access.

---

## 🧪 API Endpoints

| Method | Endpoint   | Description              |
|--------|------------|--------------------------|
| GET    | `/`        | Health check             |
| GET    | `/mail`    | Get AI summary of emails |

---

## 📄 License

MIT License. Feel free to modify and contribute!

---

## 🙌 Credits

- [FastAPI](https://fastapi.tiangolo.com/)
- [Google Generative AI](https://ai.google.dev/)
- [discord.py](https://discordpy.readthedocs.io/)
- [imap-tools](https://github.com/ikvk/imap_tools)

---

## ✨ Future Enhancements

- OAuth for Gmail login
- Web UI dashboard for summaries
- Reply or act on email via bot

---

_Ready to make your inbox smarter? Let MailBell handle the clutter._ 🧠📥
