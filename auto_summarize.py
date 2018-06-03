# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 22:01:13 2018

@author: Study Mode
"""

import requests #downloads webpage
from lxml import html
from bs4 import BeautifulSoup

url = "https://uwaterloo.ca/stories/waterloo-ranked-1-school-canada-computer-science-engineering"
page = requests.get(url)
tree = html.fromstring(page.content)
tree.xpath('//p/text()')
text = ' '.join(tree.xpath('//p/text()'))
