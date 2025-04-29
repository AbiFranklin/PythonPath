import shutil, os
from pathlib import Path

# def rename_file(source, new_name):
#     try:
#         # Extract the directory from the source path
#         directory = '/'.join(source.split('/')[:-1])
#         # Create the new file path
#         new_path = f"{directory}/{new_name}"
#         # Rename the file
#         shutil.move(source, new_path)
#         print(f"File renamed from {source} to {new_path}")
#     except Exception as e:
#         print(f"Error occurred while renaming file: {e}")

# def rename_file(source, new_name):
#     os.rename(source, new_name)

def rename_file(source, new_name):
    f = Path(source)
    f.rename(new_name)


def rename_folder(source, new_name):
    try:
        # Extract the directory from the source path
        directory = '/'.join(source.split('/')[:-1])
        # Create the new folder path
        new_path = f"{directory}/{new_name}"
        # Rename the folder
        shutil.move(source, new_path)
        print(f"Folder renamed from {source} to {new_path}")
    except Exception as e:
        print(f"Error occurred while renaming folder: {e}")


rename_file('./Working with Files in Python 3/Copy Files Copy.py', './Working with Files in Python 3/Renamed_Copying_Files_Copy.py')
rename_folder('./Working With Files in Python 3/files_to_read_copy', 'Renamed_files_to_read_copy')
