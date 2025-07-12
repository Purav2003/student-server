from dotenv import load_dotenv
import os

load_dotenv()

class Env:
    DATABASE_URL = os.getenv("DATABASE_URI")
    SECRET_KEY = os.getenv("SECRET_KEY")
    ALGORITHM = os.getenv("ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 43200)) 