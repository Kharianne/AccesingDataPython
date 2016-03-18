import xml.etree.ElementTree as ET
from xml.dom import minidom
import urllib.request
from bs4 import *
import re

def prettify(elem):
    rough_string = ET.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

def read_page(url):
    global soup, tags
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html)
    return soup

idV = 1
linkV = ""
nameV = ""
regionV = "Brno"
salaryV = ""
descriptionV = ""
pubdateV = ""
updatedV = ""

read_page("http://www.acantha.cz/category/volne-pozice/page/2/")
urls = soup.select("div.post-content-container > h2.entry-title > a")
print(urls)

url = "http://www.acantha.cz/java-programator-junior-nebo-senior/"
read_page(url)

nameV = soup.h1.string.strip()

contentTags = soup.find_all("div", class_="post-content")
for element in contentTags:
    descriptionV = element.get_text()

jobs = ET.Element("jobs")
job = ET.SubElement(jobs,"job")
job.set("id", str(idV))
link = ET.SubElement(job,"link")
link.text = "![CDATA[" + linkV + "]]"
name = ET.SubElement(job,"name")
name.text = "![CDATA[" + nameV + "]]"
region = ET.SubElement(job, "region")
region.text = "![CDATA[" + regionV + "]]"
salary = ET.SubElement(job,"salary")
salary.text = "![CDATA[" + salaryV + "]]"
description = ET.SubElement(job,"description")
description.text = "![CDATA[" + descriptionV + "]]"
pubdate = ET.SubElement(job,"pubdate")
pubdate.text = "![CDATA[" + pubdateV + "]]"
updated = ET.SubElement(job, "updated")
updated.text = "![CDATA[" + updatedV + "]]"



#print (prettify(jobs))
