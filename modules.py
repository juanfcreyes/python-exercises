import os

def extcount(path):
    files_dictionary = {}
    for file_name in os.listdir(path):
        ext = file_name.split('.')[len(file_name.split('.')) - 1]
        if ext in files_dictionary:
            files_dictionary[ext] = files_dictionary[ext] + 1
        else:
            files_dictionary.setdefault(ext, 1)
    return files_dictionary

def getfileinfo(path):
    for file_name in os.listdir(path):
        infofile = os.stat(path+'\\'+file_name)
        print(file_name + "\t"+ str(infofile.st_size) + "\t" + str(infofile.st_mtime_ns))

def list_files(path, espace):
    files = list(enumerate(os.scandir(path)))
    for tup in files:
        character = "\--" if tup[0] == (len(files) - 1) else "|--"
        if tup[1].is_dir():
            print(espace, character, tup[1].name, sep="")
            list_files(tup[1].path, "   ")
        else:
            print(espace, character, tup[1].name, sep="")

def dirtree(path):
    print(path.split("\\")[len(path.split("\\")) - 1])
    list_files(path, "")

print(os.listdir(os.getcwd()))
print(extcount(os.getcwd()))
getfileinfo(os.getcwd())

dirtree(os.getcwd())



