import os

from utils import sys_path_insert, load_dotenv

# sys_path_insert(Path(__file__).parent.parent) # projects root
sys_path_insert() # projects root

load_dotenv()

DB_USER_NAME = os.environ.get("DB_USER_NAME")
DB_USER_PASSWORD = os.environ.get("DB_USER_PASSWORD")
DB_NAME = os.environ.get("DB_NAME")