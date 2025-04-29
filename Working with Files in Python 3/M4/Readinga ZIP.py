import zipfile

def read_zip(zipf):
    with zipfile.ZipFile(zipf, 'r') as archive:
        # List all files in the zip archive
        file_list = archive.namelist()
        print("Files in the ZIP archive:")
        for file in file_list:
            info = archive.getinfo(file)
            print(f"File: {file} => Size: {info.file_size} bytes, Compressed Size: {info.compress_size} bytes")

read_zip('./files_to_zip.zip')