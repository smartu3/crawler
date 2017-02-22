#-*- coding:utf-8 -*-

from urllib.request import urlopen
from bs4 import BeautifulSoup as BS

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BS(html)
namelist = bsObj.findAll("span",{"class":"green"})
for name in namelist:
	print(name.get_text())