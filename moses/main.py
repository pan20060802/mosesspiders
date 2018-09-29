# -*- coding: utf-8 -*-
# @Time    : 2018/9/29 16:56
# @Author  : Moses
# @Email   : 269258169@.com
# @File    : main.py
# @Software: PyCharm

from scrapy import cmdline
cmdline.execute('scrapy crawl douban_spider'.split())