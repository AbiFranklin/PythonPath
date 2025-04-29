import os, fnmatch


def match(fld, search):
    for fn in os.listdir(fld):
        if fnmatch.fnmatch(fn, search):
            print(fn)


match("./Working with Files in Python 3/files", "*2_*_*.*")
