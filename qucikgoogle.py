#!/usr/bin/env python
# this line along shoud work on linux but not on Windos! just realize that.... 
# -*- coding: utf-8 -*-

"""
google something and open the top five search results
"""

import requests
import webbrowser
import bs4
import sys

search_link = 'http://google.com/search?q=' + ' '.join(sys.argv[1:])
webbrowser.open(search_link)

res = requests.get(search_link)
soup = bs4.BeautifulSoup(res.text)

link_elems = soup.select('.r a')

num_open = min(5, len(link_elems))

for i in range(num_open):
    webbrowser.open('http://google.com' + link_elems[i].get('href'))