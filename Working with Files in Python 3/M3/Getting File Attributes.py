import os
from datetime import datetime

def get_date(timestamp):
    return datetime.fromtimestamp(timestamp).strftime('%d %m %Y')

def get_file_attributes(fld):
    with os.scandir(fld) as entries:
        for entry in entries:
            if entry.is_file():
                file_info = os.stat(entry.path)
                size = file_info.st_size
                created = get_date(file_info.st_birthtime)
                modified = get_date(file_info.st_mtime)
                accessed = get_date(file_info.st_atime)
                
                print(f"File: {entry.name}")
                print(f"Size: {size} bytes")
                print(f"Created: {created}")
                print(f"Modified: {modified}")
                print(f"Accessed: {accessed}")
                print("-" * 40)

get_file_attributes('./Working with Files in Python 3/files')