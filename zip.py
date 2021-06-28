import zipfile
import os

list_name = os.listdir(os.getcwd() + "\html")
file = zipfile.ZipFile('html.zip',"w")
for name in os.listdir(os.getcwd() + "\html"):
    file.write(os.getcwd()+"\html\\" + name)
file.close()

