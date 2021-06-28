import os

def dirtree(path, name, prefij = '', dirprefij = ''):
    print(dirprefij + name + '/')
    dirprefij = prefij + '|-- '
    for name in os.listdir(path):
        path_compuesto = path+'\\'+name
        if os.path.isdir(path_compuesto):
            dirtree(path_compuesto, name, prefij + '|  ', dirprefij)
        else:
            print(dirprefij + name)

dirtree('D:\Repositorios\Python', 'Python')
    
    
