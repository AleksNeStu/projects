import os
from pathlib import Path

import dotenv

from utils import sys_path_insert

# sys_path_insert(Path(__file__).parent.parent) # projects root
sys_path_insert() # projects root

dotenv.load_dotenv(".env")  # equal to dotenv.load_dotenv("./.env")# equal to dotenv.load_dotenv("./.env")
dotenv.load_dotenv("/sec/sec.env")

DB_USER_NAME = os.environ.get("DB_USER_NAME")
DB_USER_PASSWORD = os.environ.get("DB_USER_PASSWORD")
DB_NAME = os.environ.get("DB_NAME")