#!/usr/bin/env python3
#import timeit
import re
import sys


def replace_link_titles(text):
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
