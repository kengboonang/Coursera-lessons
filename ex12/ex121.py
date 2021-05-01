# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span')
num = list()
import re
for tag in tags:
    # Look at the parts of a tag
    st = str(tag)
    regex = re.findall('([0-9]+)', st)
    if len(regex) == 0: continue
    for el in regex:
        sre = int(el)
        num.append(sre)
print(sum(num))
