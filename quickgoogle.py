#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
google something and open the top five search results
"""

import requests
import webbrowser
import bs4
import sys

if (len(sys.argv) >= 3) & (sys.argv[1] == '--top'):
    top_num = int(sys.argv[2])
    search_keyword = ' '.join(sys.argv[3:])
else:
    top_num = 5
    search_keyword = ' '.join(sys.argv[1:])
        

search_link = 'http://google.com/search?q=' + search_keyword
webbrowser.open(search_link)

res = requests.get(search_link)
soup = bs4.BeautifulSoup(res.text)

link_elems = soup.select('.r a')

num_open = min(top_num, len(link_elems))

for i in range(num_open):
    webbrowser.open('http://google.com' + link_elems[i].get('href'))