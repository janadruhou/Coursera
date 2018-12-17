import urllib.request
import json

url = "http://py4e-data.dr-chuck.net/comments_147853.json"
dcd = urllib.request.urlopen(urllib.request.Request(url)).read().decode('utf-8')
data = json.loads(dcd)
counts = list()

comments = data['comments']
for comment in comments:
    counts.append(comment['count'])

print (sum(counts))