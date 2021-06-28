import os

def readfiles(filenames):
    for f in filenames:
        for line in open(f, 'r', encoding='utf8', errors='ignore'):
            yield line

def iterfile(path):
    for direntry in os.scandir(path):
        if direntry.is_dir() is True:
            yield from iterfile(direntry.path)
        else :
            yield direntry.path

def findfiles(path):
    print("main path", path)
    for file in iterfile(path):
        print(file)

def computefiles(path):
    count = len([name for name in iterfile(path) if ".py" in name])
    print(count)

def filterfiles(path):
    python_files = (path_name for path_name in iterfile(path) if ".py" in path_name)
    for line in readfiles(python_files):
        yield line

def numberoflines(path):
    count = 0
    for line in filterfiles(path):
        count += 1
    print(count)

def numberofcodelines(path):
    count = 0
    for line in filterfiles(path):
        if len(line.strip()) > 0 and not line.startswith("#"):
            count += 1
    print(count)

print("findfiles")
findfiles("D:\\Repositorios\\Python")
print("computefiles")
computefiles("D:\\Repositorios\\Python")
print("numberoflines")
numberoflines("D:\\Repositorios\\Python")
print("numberofcodelines")
numberofcodelines("D:\\Repositorios\\Python\\pip")

