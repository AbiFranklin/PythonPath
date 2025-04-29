import zipfile

to_add = ['./Working with Files in Python 3/files/01_file.csv', './Working with Files in Python 3/files/01_file.txt']

def add_files_to_zip(zip_filename, files_to_add, opt):
    with zipfile.ZipFile(zip_filename, opt) as archive:
        for file in files_to_add:
            lst = archive.namelist()
            if file not in lst:
                archive.write(file)
                print(f"Added {file} to {zip_filename}")
            else:
                print(f"{file} already exists in {zip_filename}")

add_files_to_zip('./Working with Files in Python 3/files_to_zip.zip', to_add, 'a')