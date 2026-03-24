#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "21866171"))
API_HASH = environ.get("API_HASH", "5788dba8f23fade5edda55948e985f06")
BOT_TOKEN = environ.get("BOT_TOKEN", "")

# Indian Proxy Config (optional)
# Format examples:
#   http://ip:port
#   http://user:pass@ip:port
#   socks5://ip:port
PROXY = environ.get("PROXY", "")  # Leave empty to disable proxy

OWNER = int(environ.get("OWNER", "1289248746"))
CREDIT = environ.get("CREDIT", "MRBERLIN")

TOTAL_USER = os.environ.get('TOTAL_USERS', '1289248746').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '1289248746').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set


