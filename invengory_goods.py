#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import time
import json
import random
import requests
from selenium import webdriver

while True:
    print 'invengory taobaoke run'
    r = requests.get('http://we.40zhe.com/api/getITBKGoods')
    if (r.status_code != 200):
        time.sleep(5)
        continue

    obj = json.loads(r.text, encoding='utf-8')
    if (len(obj) == 0):
        time.sleep(5)
        continue

    for item in obj['data']:
        driver = webdriver.Chrome()
        driver.get(item['taobaoke_url'])

        try:
            try:
                ele = driver.find_element_by_name("item_id")
                itemId = ele.get_attribute("value")
                img = driver.find_element_by_id('J_ImgBooth').get_attribute("src")
            except:
                ele = driver.find_element_by_id("LineZing")
                itemId = ele.get_attribute("itemid")
                img = driver.find_element_by_id('J_ImgBooth').get_attribute("src")

            print 'taobaoke : %s' % item['taobaoke_url']
            print 'taobaoId: %s' % itemId
            title = driver.title.replace('-淘宝网', '')
            title = title.replace('-tmall.com天猫', '')
            url = 'http://we.40zhe.com/api/setITBKGoods?inventory_goods_id=%s&item_id=%s&title=%s&item_pic=%s' % (item['inventory_goods_id'], itemId, title, img)
            print 'taobaoId crawl : %s' % url.encode('utf-8')
            rs = requests.get(url)
            print rs.status_code
        except Exception as e:
            print 'delete goods'
            url = 'http://we.40zhe.com/api/deleteITBKGoods?inventory_goods_id=%d' % (item['inventory_goods_id'])
            print 'delete goods: %s' % url.encode('utf-8')
            rs = requests.get(url)
            print rs.status_code

        # rand = random.randint(5, 8)
        # print 'sleep : %s' % rand
        # time.sleep(rand)
        driver.quit()
