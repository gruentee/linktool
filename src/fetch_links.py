#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup as bs
import requests

# Base URL for Trotec site
BASE_URL = "http://de.trotec.com/"
# Parameters to fetch XML version of TYPO3 page
PAYLOAD = { "type": 105 }

"""Get TYPO3 pageId from link"""
def get_page_id(link):
    r = requests.get(link, params=PAYLOAD)
    soup = bs(r.content, 'lxml-xml')
    return soup.find('PageInfo')['uid']