import zipfile

to_zip = ['./Working with Files in Python 3/files/subfolder/01_file_test.csv', 
          './Working with Files in Python 3/files/subfolder/01_file_test.txt', 
          './Working with Files in Python 3/files/subfolder/01_test_file.csv', 
          './Working with Files in Python 3/files/subfolder/01_test_file.txt', 
          './Working with Files in Python 3/files/01_file_test.csv',
          './Working with Files in Python 3/files/01_file_test.txt',]

def create_zip(zip_name, files_to_zip,opt):
    with zipfile.ZipFile(zip_name, opt, allowZip64=True) as archive:
        for file in files_to_zip:
            archive.write(file)
            print(f"Added {file} to {zip_name}")

create_zip('./Working with Files in Python 3/files_to_zip.zip', to_zip, 'w')  # 'w' for write mode