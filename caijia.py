# coding=utf-8 
import requests 

import re


from lxml import etree

import urllib
from bs4 import BeautifulSoup


url='http://www.hzjg.gov.cn/hzzs'
resp=urllib.request.urlopen(url)
html=resp.read()


bs=BeautifulSoup(html)

items=bs.find_all('table')



items2=items[0].find_all('tr')


for i in items2:
	items3=i.find_all('td')
	
	print('++++++++++++++++++++++++\n')
	
	
	str=items3[0].text+'++-----'+items3[3].text
	print(str)
		



