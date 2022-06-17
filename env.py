import os
from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv("API_ID", "11508502").strip()
API_HASH = os.getenv("API_HASH", "3e6e5be80d5c89ff19b5e5fb7bfaa0f4").strip()
BOT_TOKEN = os.getenv("BOT_TOKEN", "5443525365:AAGGUw3_qmi2PzfRG5GGS9wCIVAwH98W4xI").strip()
DATABASE_URL = os.getenv("DATABASE_URL", "").strip()
MUST_JOIN = os.getenv("MUST_JOIN", "TheXCodeTeam")

if not API_ID:
    print("No API_ID found. Exiting...")
    raise SystemExit
if not API_HASH:
    print("No API_HASH found. Exiting...")
    raise SystemExit
if not BOT_TOKEN:
    print("No BOT_TOKEN found. Exiting...")
    raise SystemExit
if not DATABASE_URL:
    print("No DATABASE_URL found. Exiting...")
    raise SystemExit

try:
    API_ID = int(API_ID)
except ValueError:
    print("API_ID is not a valid integer. Exiting...")
    raise SystemExit

if 'postgres' in DATABASE_URL and 'postgresql' not in DATABASE_URL:
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")
