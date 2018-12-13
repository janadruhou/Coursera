import urllib
from bs4 import BeautifulSoup

web = 'http://py4e-data.dr-chuck.net/known_by_Mercy.html'
data = urllib.urlopen(web).read()
count = int(raw_input('Enter count:'))
position = int(raw_input('Enter position:'))-1


BS = BeautifulSoup(data,"html.parser")
href = BS('a')

for i in range(count):
    link = href[position].get('href', None)
    print href[position].contents[0]
    data = urllib.urlopen(link).read()
    BS = BeautifulSoup(data,"html.parser")
    href = BS('a')