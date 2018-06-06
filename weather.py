import urllib.request, json

baseurl = "https://query.yahooapis.com/v1/public/yql?"

result = baseurl #+ "&format= json"

res = urllib.request.urlopen(result).read()
data = json.load(res)

print (data)