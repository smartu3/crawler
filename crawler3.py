#-*- coding:utf-8 -*-

from urllib.request import urlopen
from bs4 import BeautifulSoup as BS
import re
import datetime
import random

html = urlopen("http://baike.baidu.com/link?url=pJVAOIqoMiEHWzZjJk21mOgjWf7bbj8bS21qaD2l5BeXj1zEa254eEEg1IgBRiksk3fZoEt12izk9fNNeLn-2bfWLcCpV5sNzWnBmEi0Z-u")
bsObj = BS(html,features="lxml")
for link in bsObj.find("div",{"class":"lemma-summary"}).findAll("a",href=re.compile("^(/(view|subview)/)((?!:).)*$")):
	if "href" in link.attrs:
		print(link.attrs['href'])
# random.seed(datetime.datetime.now())
# def getLinks(articleUrl):
	# html = urlopen("http://baike.baidu.com