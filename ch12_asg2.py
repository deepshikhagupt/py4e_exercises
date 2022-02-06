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

url = input('Enter URL')
count = input('Enter count:')
position = input('Enter position:')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
#tags = soup('a')


for i in range(int(count)):
    html = urllib.request.urlopen(new_url, context=ctx).read()
    new_url = BeautifulSoup(html, 'html.parser')
    tags = new('a')
    index = 0
    for tag in tags:
        index += 1
        if index == position:
            #print('Retrieving:', url)
            new_url = tag.get('href', None)
            print('Retrieving:',tag.get(new_url)
