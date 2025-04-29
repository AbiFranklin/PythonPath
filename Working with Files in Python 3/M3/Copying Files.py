import shutil

def copy_file(source, destination):
    try:
        shutil.copy(source, destination)
        print(f"File copied from {source} to {destination}")
    except Exception as e:
        print(f"Error occurred while copying file: {e}")

def copy_folders(source_folder, destination_folder):
    try:
        shutil.copytree(source_folder, destination_folder)
        print(f"Folder copied from {source_folder} to {destination_folder}")
    except Exception as e:
        print(f"Error occurred while copying folder: {e}")

copy_file('./Working with Files in Python 3/M3/Copying Files.py', './Working with Files in Python 3/files/Copying Files Copy.py')
copy_folders('./Working with Files in Python 3/files_to_read', './Working with Files in Python 3/files/files_to_read_copy')