import os

class Config(object):
    # هنا نقرأ البيانات من Render (متغيرات البيئة)
    # ما نكتب بيانات حقيقية هنا!
    
    TOKEN = os.getenv("TOKEN")  # سيقرأ من Render
    API_ID = int(os.getenv("API_ID", 0))
    API_HASH = os.getenv("API_HASH")
    OWNER_ID = int(os.getenv("OWNER_ID", 0))
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    
    LOGGER = True
    ALLOW_CHATS = True
    LOAD = []
    NO_LOAD = ["rss", "cleaner", "connection", "math"]

class Production(Config):
    LOGGER = True

class Development(Config):
    LOGGER = True
