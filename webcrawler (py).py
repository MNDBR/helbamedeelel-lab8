# -*- coding: utf-8 -*-
"""WebCrawler

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1A0pc3GRNtG4GXCkCkpje7vfoLgONSMsT
"""

import requests
from bs4 import BeautifulSoup

url = 'https://news.xopom.com/285707/'
res = requests.get(url)
html_page = res.content
soup = BeautifulSoup(html_page, 'html.parser')
text = soup.find_all(text=True)

output = ''
blacklist = [
	'[document]',
	'noscript',
	'header',
	'html',
	'meta',
	'head', 
	'input',
	'script',
	# there may be more elements you don't want, such as "style", etc.
]

for t in text:
	if t.parent.name not in blacklist:
		output += '{} '.format(t)

print(output)









