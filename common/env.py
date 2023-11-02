import os
import dotenv

dotenv.load_dotenv()  # equal to dotenv.load_dotenv("./.env")
dotenv.load_dotenv("/sec/sec.env")

DB_USER_NAME = os.environ.get("DB_PASS")