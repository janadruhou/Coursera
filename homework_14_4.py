import urllib.request, urllib.parse, urllib.error
import json
import ssl
import http
import sqlite3
import time

source = "http://py4e-data.dr-chuck.net/json?"

test_institution = "South Federal University"
my_institution = "Indiana University at Bloomington"

while True:
    address = input('Enter institution: ')
    if len(address) < 1: break
    
    parms = {"address": address}
    
    url = source + urllib.parse.urlencode(parms)

    print ('Digging', url)
    data = urllib.request.urlopen(url).read().decode()
    print("Fetched", len(data), 'characters')

    fetched = json.loads(data)

    print(fetched)
    