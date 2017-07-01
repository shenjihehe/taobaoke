#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import os
import requests
import json
from selenium import webdriver


r = requests.get('http://article.app/api/getAllArticles')
if (r.status_code != 200):
    os._exit(0)

obj = json.loads(r.text, encoding='utf-8')
if (len(obj) == 0):
    os._exit(0)

driver = webdriver.Chrome()
for item in obj:
    driver.get(item['taobaoke_url'])
    try:
        try:
            ele = driver.find_element_by_name("item_id")
            itemId = ele.get_attribute("value")
        except:
            ele = driver.find_element_by_id("LineZing")
            itemId = ele.get_attribute("itemid")

        print 'taobaoke : %s' % item['taobaoke_url']
        title = driver.title.replace('-淘宝网', '')
        title = title.replace('-tmall.com天猫', '')
        url = 'http://article.app/api/setArticleAttr?id=%s&taobao_id=%s&title=%s' % (item['id'], itemId, title);
        print 'crawl : %s' % url.encode('utf-8')
        rs = requests.get(url)
        print rs.status_code
    except Exception as e:
        url = 'http://article.app/api/deleteArticle?id=%s' % item['id'];
        rs = requests.get(url)
        print 'delete %s' % item['id']
        print e

driver.quit()
