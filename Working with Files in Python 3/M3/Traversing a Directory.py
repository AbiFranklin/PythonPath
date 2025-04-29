import os

def traverse_directory(fld):
    for fldpath, dirs, fls in os.walk(fld):
        print(f"Directory: {fldpath}")
        for dir_name in dirs:
            print(f"  Subdirectory: {dir_name}")
        for file_name in fls:
            print(f"  File: {file_name}")

traverse_directory('./Working with Files in Python 3/files')