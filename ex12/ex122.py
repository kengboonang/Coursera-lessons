# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
count = input('Enter count: ')
pos = input('Enter position: ')
counts = 0

#My code for finding pos 18
tags = soup('li')
num = list()
import re

#Finding all the names
for tag in tags:
    st = str(tag)
    regex = re.findall('href="(.+)"', st)
    if len(regex) == 0: continue
    for el in regex:
        num.append(el)

#Finding pos 18
x = int(pos) - 1
print('Retreiving: ', num[int(x)])
counts = counts + 1


while int(count) > int(counts):
    url = num[int(x)]
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    #My code for finding pos 18
    tags = soup('li')
    num = list()
    import re

    #Finding all the names
    for tag in tags:
        st = str(tag)
        regex = re.findall('href="(.+)"', st)
        if len(regex) == 0: continue
        for el in regex:
            num.append(el)

    #Finding pos 18
    x = int(pos) - 1
    print('Retreiving: ', num[int(x)])
    counts = counts + 1
