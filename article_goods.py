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

# 转换淘宝客链接、抓取:图片、ID、标题
while True:
    print 'conver article taobaoke_url, crawl image id title.'

    try:
        r = requests.get('http://we.40zhe.com/api/getAllArticles')
    except Exception as e:
        time.sleep(10)
        print e
        continue

    if (r.status_code != 200):
        time.sleep(5)
        continue

    obj = json.loads(r.text, encoding='utf-8')
    if (len(obj) == 0):
        time.sleep(5)
        continue


    for item in obj:
        try:
            driver = webdriver.Chrome()
            driver.get(item['taobaoke_url'])
        except:
            continue

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
            title = driver.title.replace('-淘宝网', '')
            title = title.replace('-tmall.com天猫', '')
            url = 'http://we.40zhe.com/api/setArticleAttr?id=%s&taobao_id=%s&title=%s&img_src=%s' % (item['id'], itemId, title, img)
            print 'crawl : %s' % url.encode('utf-8')
            rs = requests.get(url)
            print rs.status_code
        except Exception as e:
            url = 'http://we.40zhe.com/api/deleteArticle?id=%s' % (item['id'])
            rs = requests.get(url)
            print 'delete taobao_id %s' % item['taobao_id']
            print rs.status_code
            print e

        driver.quit()

    rand = random.randint(5, 8)
    print 'sleep : %s' % rand
    time.sleep(rand)

