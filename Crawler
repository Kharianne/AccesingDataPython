import urllib.request
import re
from bs4 import *
soup = None
tags = None

i = 0

count_input = input("Enter count: ")
count = int(count_input)
position_input = input("Enter position: ")
position = int(position_input)
def read_page(go_to_url):
    global soup, tags
    #url = "http://python-data.dr-chuck.net/known_by_Fikret.html"
    html = urllib.request.urlopen(go_to_url).read()
    soup = BeautifulSoup(html)
    tags = soup('a')
    return tags

read_page("http://python-data.dr-chuck.net/known_by_Samanthalee.html")

while i in range(count):
    urls = []
    names = []
    for tag in tags:
        url = tag.get('href', None)
        urls.append(url)
        name = re.findall('known_by_(.+)\.html',url)
        names.extend(name)
    go_to_url = urls[position - 1]
    print (names[position - 1])
    read_page(go_to_url)
    i = i + 1