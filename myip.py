from urllib.request import urlopen
import json
request = urlopen("http://httpbin.org/get")
response = request.read()
print(json.loads(response)['origin'])
