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
        r = requests.get('http://we.40zhe.com/api/getAllArticlesNoneImage')
    except Exception as e:
        time.sleep(10)
        print e
        continue

    if (r.status_code != 200):
        time.sleep(5)
        continue

    try:
        item = json.loads(r.text, encoding='utf-8')
        if (len(item) == 0):
            time.sleep(5)
            continue
    except Exception as e:
        time.sleep(2)
        continue



    driver = webdriver.Chrome()

    try:
        driver.get(item['taobaoke_url'])
    except:
        url = 'http://we.40zhe.com/api/deleteArticle?id=%s' % (item['id'])
        rs = requests.get(url)
        print 'Request Url Error'
        print 'Delete taobaoke url %s' % item['taobaoke_url']
        print url
        driver.quit()
        continue

    try:
        try:
            # 淘宝
            ele = driver.find_element_by_name("item_id")
            itemId = ele.get_attribute("value")
            img = driver.find_element_by_id('J_ImgBooth').get_attribute("src")
            price = driver.find_element_by_class_name('tb-rmb-num').text
        except:
            # 天猫
            ele = driver.find_element_by_id("LineZing")
            itemId = ele.get_attribute("itemid")
            img = driver.find_element_by_id('J_ImgBooth').get_attribute("src")
            price = driver.find_element_by_class_name('tm-price').text

        print 'taobaoke : %s' % item['taobaoke_url']
        title = driver.title.replace('-淘宝网', '')
        title = title.replace('-tmall.com天猫', '')
        url = 'http://we.40zhe.com/api/setArticleAttr?id=%s&taobao_id=%s&title=%s&img_src=%s&price=%s' % (item['id'], itemId, title, img, price)
        print 'crawl : %s' % url.encode('utf-8')
        rs = requests.get(url)
        print rs.status_code
        driver.quit()
    except Exception as e:
        print 'Request Url Error'
        print 'Delete taobao url %s' % item['taobaoke_url']
        print e
        url = 'http://we.40zhe.com/api/deleteArticle?id=%s' % (item['id'])
        rs = requests.get(url)
        print url
        driver.quit()


    rand = random.randint(3, 15)
    print 'sleep : %s' % rand
    time.sleep(rand)

    driver.quit()

