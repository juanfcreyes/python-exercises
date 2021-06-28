from bs4 import BeautifulSoup
from urllib.request import urlopen

url = 'http://www.python.org/'
response = urlopen(url)
content = response.read().decode('UTF-8')
soup = BeautifulSoup(content, 'html.parser')

for link in soup.find_all('a'):
    print(link.get('href'))
    
print(len(soup.find_all('a')))
