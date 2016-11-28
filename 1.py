#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import re

from bs4 import BeautifulSoup


def find_num(str):
    pattern = r'\d{5}'
    result = re.search(pattern, str)
    if result is not None:
        return result.group()
    else:
        return None


if __name__ == '__main__':
    url = 'http://www.heibanke.com/lesson/crawler_ex00/'
    num = ''

    while num is not None:
        print('url: %s' % url + num)
        request = urllib2.Request(url + num)
        response = urllib2.urlopen(request)
        rep_body = response.read()
        soup = BeautifulSoup(rep_body, 'lxml')
        num = find_num(soup.find_all('h3')[0].encode('utf-8'))
    print('Done.')