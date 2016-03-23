#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 19:58:30 2016

@author: connzen
"""

# TODO: write tests

def replace_links(html):
    from bs4 import BeautifulSoup as bs
    #html = open('test.html', 'r').read()
    soup = bs(html, 'html.parser')
    for link in soup.find_all('a'):
        link['title'] = link.text
    return str(soup)

def replace_link_(text):
    pattern = "<a[^>]*?title=\"([^\"]*?)\"[^>]*?>([^<]*)<\/a>"
    regex = re.compile(pattern)
    matches = regex.findall(text, re.UNICODE)
    for m in matches:
        text = text.replace(m[0], m[1])
    return text

# TODO: alternative implementation with re.sub()
        

#for m in regex.finditer(text, re.UNICODE):
    #print(match)
    #print(m.group())
#    print(m.group(1))
#    print(m.group(2))
#    text = text.replace(m.group(1), m.group(2))
#    text = text[:m.start(1)] + m.group(2) + text[m.end(1):]
