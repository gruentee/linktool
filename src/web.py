#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 20:20:49 2016

@author: connzen
"""

from bottle import Bottle, route, run, template, static_file, request
from replace_links import replace_links
from fetch_links import get_page_id
#from regex_replace import replace_link_titles

app = Bottle()

@app.route('/<filename:path>')
def index(filename):
    return static_file(filename, root='../web/assets/')

@app.post('/replace-links')
def return_links():
    text = request.forms.get('text')
    return replace_links(text).encode('latin-1')
    
@app.post('/get-page-id')
def return_page_id():
    # TODO: input validation
    page_id = get_page_id(request.forms.get('input-link'))
    return page_id

run(app, host='localhost', port='61004', reloader=True)
