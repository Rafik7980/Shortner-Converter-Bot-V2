# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "24401700"))
API_HASH = os.environ.get("API_HASH", "ec67ae4aa1daff513fe12f8cac156b17")
BOT_TOKEN = os.environ.get("5922718859:AAHhbTYqcebKNAyieWgVWn83HqK7NH_TcEc")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split("-1001502874809")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("aglink", "Db Name")
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://cluster0.uf0d2nk.mongodb.net/myFirstDatabase" --apiVersion 1 --username mdrafikgouri") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "-1001682855227")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(Id Owned Id)
#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001488908827")) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "aglinkss Without @") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", '') # image when someone hit /start # image when someone hit /start
LINK_BYPASS = "False"
