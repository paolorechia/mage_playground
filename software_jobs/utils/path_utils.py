import os
from software_jobs.utils.date_utils import get_today_string

def get_today_remotive_path():
    now = get_today_string()
    filepath = f'/data/{now}_remotive.json'

    return filepath

def remotive_file_exists() -> bool:
    filepath = get_today_remotive_path()
    return os.path.exists(filepath)