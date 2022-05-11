import os
from dotenv import load_dotenv

DIRNAME = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(DIRNAME, "..", ".env"))
except FileNotFoundError:
    pass

DB_NAME = os.getenv('DATABASE_FILENAME') or 'database.sqlite'
DB_PATH = os.path.join(DIRNAME, DB_NAME)
