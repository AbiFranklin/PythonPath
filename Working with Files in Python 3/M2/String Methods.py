import os


def ends_with(fld, suffix):
    for fn in os.listdir(fld):
        if fn.endswith(suffix):
            print(f"{fn}")


def starts_with(fld, prefix):
    for fn in os.listdir(fld):
        if fn.startswith(prefix):
            print(f"{fn}")


ends_with("./Working with Files in Python 3/files", ".txt")
print("\n\n")
starts_with("./Working with Files in Python 3/files", "02")
