import urllib

from bs4 import BeautifulSoup

#preparation of data from web site
web = 'http://py4e-data.dr-chuck.net/comments_147850.html'
data = urllib.urlopen(web).read()
BS = BeautifulSoup(data,'html.parser')
lines = BS('span')

#sumation via forcycle
sums = 0
for tags in lines:
    sums = sums + int(tags.contents[0])

print(sums)