import os

def readfile(filename):
    for line in open(filename, 'r', encoding='utf8', errors='ignore'):
        yield line

def writefile(name_file, data):
     f = open(name_file, 'w')
     f.write("".join(data))

def split(path, n):
    container = []
    counter = 0
    num_partition = 1
    for line in readfile(path):
        if counter > n:
            writefile("split" + str(num_partition) + ".txt", container)
            counter = 0
            container = []
            num_partition += 1
        else:
            container.append(line)
        counter += 1

    if len(container) > 0:
       writefile("split" + str(num_partition) + ".txt", container)  
    print(num_partition)

split("D:\\Repositorios\\Python\\oop\\findfiles.py", 10)
