#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
import urllib2
import re
import cookielib

from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    'Referer': 'http://www.heibanke.com/lesson/crawler_ex01/'
}


if __name__ == '__main__':
    url = 'http://www.heibanke.com/lesson/crawler_ex01/'

    cookies = cookielib.CookieJar()
    handler = urllib2.HTTPCookieProcessor(cookies)
    opener = urllib2.build_opener(handler)
    response = opener.open(url)

    csrf_token = ''
    for cookie in cookies:
        if cookie.name == 'csrftoken':
            csrf_token = cookie.value

    for pwd in range(1, 31):
        print('try password: %d' % pwd)

        values = {'username': 'username', 'password': pwd, 'csrfmiddlewaretoken': csrf_token}
        data = urllib.urlencode(values)

        request = urllib2.Request(url, data, headers)
        try:
            response = opener.open(request)
        except urllib2.HTTPError, e:
            print('HTTP error: %s' % e.code)
        except urllib2.URLError, e:
            print('URL error: %s' % e.reason)
        else:
            rep_body = response.read()

        soup = BeautifulSoup(rep_body, 'lxml')

        pattern = re.compile(ur'错误', re.UNICODE)
        if pattern.search(soup.get_text()) is None:
            break

    print('Done.')