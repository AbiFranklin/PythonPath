import shutil

def move_file(source, destination):
    try:
        shutil.move(source, destination)
        print(f"File moved from {source} to {destination}")
    except Exception as e:
        print(f"Error occurred while moving file: {e}")

def move_folder(source, destination):
    try:
        shutil.move(source, destination)
        print(f"Folder moved from {source} to {destination}")
    except Exception as e:
        print(f"Error occurred while moving folder: {e}")


move_file('./Working With Files in Python 3/files/Copying Files Copy.py', './Working With Files in Python 3/Copy Files Copy.py')
move_folder('./Working With Files in Python 3/files/files_to_read_copy', './Working With Files in Python 3/')