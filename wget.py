from urllib.request import urlopen
import sys


url = 'http://www.python.org/'
if (len(sys.argv) > 1):
    url = sys.argv[1]
    
print(url)
response = urlopen(url)
print(response.headers)
content = response.read().decode('UTF-8')
name = url.split('/')[-1].split('.')[0]
filename = "html/" + (name + ".html" if len(name) > 0 else "index.html")
f = open(filename, 'w')
f.write(content)
f.close()



