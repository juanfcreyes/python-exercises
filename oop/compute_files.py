import os

def computefiles(path):
    count = 0
    for direntry in os.scandir(path):
        if direntry.is_dir() is True:
            count = count + computefiles(direntry.path)
        else:
            if ".py" in direntry.name:
                count += 1
    return count

print(computefiles("D:\\Repositorios\\Python"))

