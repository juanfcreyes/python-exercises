import os

def print_path(files):
    for file in files:
        print(file)

def findfiles(path):
    print("main path", path)
    for direntry in os.scandir(path):
        if direntry.is_dir() is True:
            print_path(findfiles(direntry.path))
        else:
            yield direntry.path

print_path(findfiles("D:\\Repositorios\\Python"))

