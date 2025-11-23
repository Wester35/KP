import os
import sys

def get_app_dir():
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    else:
        return os.path.dirname(os.path.abspath(__file__))

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATA_DIR = os.path.join(get_app_dir(), "data")
IMAGES_DIR = os.path.join(DATA_DIR, "user_images")
SESSION_FILE = os.path.join(DATA_DIR, "user_session.json")
DB_CONFIG_FILE = os.path.join(DATA_DIR, "db_config.json")