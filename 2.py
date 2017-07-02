#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import time
import requests
import json
from selenium import webdriver

while True:
    print 'invengory taobaoke run'
    r = requests.get('http://article.app/api/getITBKGoods')
    if (r.status_code != 200):
        time.sleep(5)
        continue

    obj = json.loads(r.text, encoding='utf-8')
    if (len(obj) == 0):
        time.sleep(5)
        continue

    driver = webdriver.Chrome()
    for item in obj['data']:
        try:
            driver.get(item['taobaoke_url'])
            try:
                ele = driver.find_element_by_name("item_id")
                itemId = ele.get_attribute("value")
            except:
                ele = driver.find_element_by_id("LineZing")
                itemId = ele.get_attribute("itemid")

            print 'crawl taobaoId: %s' % itemId
            url = 'http://we.40zhe.com/api/setITBKGoodsr?inventory_goods_id=%s&item_id=%s' % (item['inventory_goods_id'], itemId)
            print 'taobaoId crawl : %s' % url.encode('utf-8')
            rs = requests.get(url)
            print rs.status_code
        except Exception as e:
            print e
            pass

    driver.quit()
