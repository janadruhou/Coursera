import urllib2

from bs4 import BeautifulSoup

web = urllib2.urlopen(input("Enter web page:" ))
su = BeautifulSoup(web, "html.parser")

sp = su('span')

nums = []

for span in sp:
    nums.append(int(sp.string))

print(sum(nums))