import zipfile

def extract_zip(zip_file_path, fn, extract_to_folder):
    """
    Extracts a specific file from a ZIP archive to a specified folder.

    Parameters:
    zip_file_path (str): The path to the ZIP file.
    fn (str): The name of the file to extract from the ZIP archive.
    extract_to_folder (str): The folder where the extracted file will be saved.

    Returns:
    None
    """
    try:
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            # Check if the file exists in the ZIP archive
            if fn in zip_ref.namelist():
                zip_ref.extract(fn, extract_to_folder)
                print(f"Extracted '{fn}' to '{extract_to_folder}'")
            else:
                print(f"File '{fn}' not found in the ZIP archive.")
    except zipfile.BadZipFile:
        print("Error: The provided file is not a valid ZIP file.")
    except Exception as e:
        print(f"An error occurred: {e}")


def extract_all(zip_file_path, extract_to_folder):
    """
    Extracts all files from a ZIP archive to a specified folder.

    Parameters:
    zip_file_path (str): The path to the ZIP file.
    extract_to_folder (str): The folder where the extracted files will be saved.

    Returns:
    None
    """
    try:
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to_folder)
            print(f"Extracted all files to '{extract_to_folder}'")
    except zipfile.BadZipFile:
        print("Error: The provided file is not a valid ZIP file.")
    except Exception as e:
        print(f"An error occurred: {e}")



extract_zip('./Working with Files in Python 3/files_to_zip.zip', 'Working with Files in Python 3/files/01_file.csv', './Working with Files in Python 3/Extracted_Files')
extract_all('./Working with Files in Python 3/files_to_zip.zip', './Working with Files in Python 3/Extracted_Files/All_Files')