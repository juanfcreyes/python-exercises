import re
from urllib.request import urlopen 

def getcontent(url):
    response = urlopen(url)
    content = response.read().decode('utf-8')
    return content

def getlinks(content):
    pattern = '<a.*'
    finded = re.findall(pattern, content)
    for link in finded:
        print(link)
    links = set([])
    for link in finded:
        m = re.search(r'(?<=href=")[^\s]*"', link)
        links.add(m.group().strip('"'))
    return sorted(list(links))

links = lambda url : getlinks(getcontent(url))

for link in links('http://www.python.org/'):
    print(link)

print(len(links('http://www.python.org/')))
  
