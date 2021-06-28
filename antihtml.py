from urllib.request import urlopen
import re
import sys
import D:/Repositorios/Python/wget.py

url = 'http://www.python.org/'
if (len(sys.argv) > 1):
    url = sys.argv[1]
    
print(url)
response = urlopen(url)
content = response.read().decode('utf-8')
name = url.split('/')[-1].split('.')[0]
filename = "html/" + (name + ".html" if len(name) > 0 else "index.html")

f = open(filename, 'w')
f.write(content)
f.close()
m = re.findall('<.+>.{1,}</.+>', content.strip(" ").strip("\n").strip("\t"))

for i in m:
    x = re.sub('<.*?>','', i)
    print(x)

    
