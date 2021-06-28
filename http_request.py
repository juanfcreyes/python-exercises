from urllib.request import urlopen
response = urlopen("http://python.org/")
print("headers", response.headers)
content = response.read()
print("content", content)
