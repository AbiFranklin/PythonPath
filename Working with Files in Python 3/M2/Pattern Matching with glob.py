from pathlib import Path


def glob_match(fld, search):
    p = Path(fld)
    for fn in p.glob(search):
        print(fn.name)


glob_match("./Working with Files in Python 3/files", "*1*.txt")

# glob differs from fnmatch in that it returns Path objects, which are more powerful and flexible than strings.
#   It also does not pull in the entire list of files in the directory into memory, making it more efficient for large directories.
