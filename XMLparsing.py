import urllib.request
import xml.etree.ElementTree as ET

go_to_url = "http://python-data.dr-chuck.net/comments_235575.xml"
xml_file = urllib.request.urlopen(go_to_url).read()

sum = 0
tree = ET.fromstring(xml_file)
comment = tree.findall('.//comment')
for child in tree.findall('.//comment'):
    count = child.find('count').text
    number = int(count)
    sum += number

print(sum)

#counts = [x.text for x in tree.findall('.//count')]
#print(counts)
