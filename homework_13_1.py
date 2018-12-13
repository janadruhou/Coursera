import urllib
import xml.etree.ElementTree as ET

web = "http://py4e-data.dr-chuck.net/comments_147852.xml"
data = urllib.urlopen(web).read()

tree = ET.fromstring(data)

num = tree.findall('comments/comment/count')

alles = 0

for nu in num:
    alles += int(nu.text)

print(alles)