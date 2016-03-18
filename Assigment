import urllib.request
import re
from bs4 import *

all_numbers = []
total = 0

url = "http://python-data.dr-chuck.net/comments_235578.html"
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html)

tags = soup('span')
for tag in tags:
    tag = tag.decode()
    numbers = re.findall('([0-9]+)', tag)
    all_numbers += numbers
for i in all_numbers:
    total += int(i)
print (total)
