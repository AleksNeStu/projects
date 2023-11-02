import os
import dotenv

dotenv.load_dotenv()  # equal to dotenv.load_dotenv("./.env")
dotenv.load_dotenv("/sec/sec.env")

DB_USER_NAME = os.environ.get("DB_USER_NAME")
DB_USER_PASSWORD = os.environ.get("DB_USER_PASSWORD")
DB_NAME = os.environ.get("DB_NAME")