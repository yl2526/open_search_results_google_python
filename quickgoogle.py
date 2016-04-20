#!/usr/bin/env python
# -*- coding: utf-8 -*-

# so far the shebang line only works for linux. 
# I hope I can find a way to make it owrk on windows.

"""
google something and open the top five search results
"""

import requests
import webbrowser
import bs4
import sys, getopt

# -t 5 and --top=5 are two ways to specify the number of top search results to open
opts, args = getopt.getopt(sys.argv[1:], "t:", ["top="])

if opts:
    opt, val = zip(*opts)
    assert all([op in ('-t', '--top') for op in opt]), 'unknow options' 
    # in case that both -t and --top= are used, only the smaller one will be used
    top_num = min([int(v) for v in val])
else:
    top_num = 5

search_keyword = ' '.join(args)  

#open the search page
search_link = 'http://google.com/search?q=' + search_keyword
webbrowser.open(search_link)

res = requests.get(search_link)
soup = bs4.BeautifulSoup(res.text)

link_elems = soup.select('.r a')

# in case that there are only a few search results, 
# take the smaller of links found and specifiedd number

num_open = min(top_num, len(link_elems))

for i in range(num_open):
    #open the top search results' links
    webbrowser.open('http://google.com' + link_elems[i].get('href'))

