import shutil, os

# def delete_file(file_path):
#     try:
#         shutil.os.remove(file_path)
#         print(f"File deleted: {file_path}")
#     except Exception as e:
#         print(f"Error occurred while deleting file: {e}")

def delete_file(f):
    if os.path.isfile(f):
        try:
            os.remove(f)
            print(f"File deleted: {f}")
        except Exception as e:
            print(f"Error occurred while deleting file: {e}")


# def delete_folder(folder_path):
#     try:
#         shutil.rmtree(folder_path)
#         print(f"Folder deleted: {folder_path}")
#     except Exception as e:
#         print(f"Error occurred while deleting folder: {e}")
            
def delete_folder(fld):
    if os.path.isdir(fld):
        try:
            shutil.rmtree(fld)
            print(f"Folder deleted: {fld}")
        except Exception as e:
            print(f"Error occurred while deleting folder: {e}")

delete_file('./Working With Files in Python 3/Renamed_Copying_Files_Copy.py')
delete_folder('./Working With Files in Python 3/Renamed_files_to_read_copy')