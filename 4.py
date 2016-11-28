#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

"""

import urllib
import urllib2
import re
import cookielib

from bs4 import BeautifulSoup


class HTTPConstant(object):
    """HTTP Constant Values.

    """

    def __init__(self):
        pass

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
        'Referer': 'http://www.heibanke.com/accounts/login/?next=/lesson/crawler_ex02/'
    }


if __name__ == '__main__':
    login_url = 'http://www.heibanke.com/accounts/login/?next=/lesson/crawler_ex02/'
    url = 'http://www.heibanke.com/lesson/crawler_ex03/'

    cookies = cookielib.CookieJar()
    handler = urllib2.HTTPCookieProcessor(cookies)
    opener = urllib2.build_opener(handler)

    opener.open(login_url)

    csrftoken = ''
    for cookie in cookies:
        if cookie.name == 'csrftoken':
            csrftoken = cookie.value

    login_req = urllib2.Request(login_url, urllib.urlencode({'username': 'iiii', 'password': '123456', 'csrfmiddlewaretoken': csrftoken}))

    opener.open(login_req)

    for pwd in range(1, 31):
        print('try password: %d' % pwd)

        for cookie in cookies:
            if cookie.name == 'csrftoken':
                csrftoken = cookie.value
        data = urllib.urlencode({'username': 'username', 'password': pwd, 'csrfmiddlewaretoken': csrftoken})

        headers['Rdferer'] = 'http://www.heibanke.com/lesson/crawler_ex03/'
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
