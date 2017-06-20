#!/usr/bin/python
# -*- coding: utf-8 -*-
"""game of words network check of words"""
# http://orfo.ruslang.ru/search/word    
import os
import re
from grab import Grab, GrabError

g = Grab(log_file='out.html')
proxy=''
if 'http_proxy' in os.environ:
    proxy = os.environ['http_proxy']

if proxy:
    g.setup(proxy=proxy, proxy_type='http', connect_timeout=5, timeout=5)

def check_word(word):
    print 'IN CHECK ',word
    g.go('http://orfo.ruslang.ru/search/word')    
    g.doc.set_input('word', word)
    g.doc.set_input('title_check', 'yes')
    g.doc.submit()

    r = g.doc.rex_text("<div class=\"col-md-10\" >([^>]+)</div>")
    print 'result ',r
    return any(char.isdigit() for char in r)

