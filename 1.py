# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import traceback
import requests
import json
from selenium import webdriver

driver = webdriver.Chrome()

r = requests.get('http://we.40zhe.com/api/getAllArticles', timeout = 9000)
if (r.status_code == 200):
    obj = json.loads(r.text, encoding='utf-8')
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
            print '-----------'
            title = driver.title.replace('-淘宝网', '')
            title.replace('-tmall.com天猫', '')
            print title
            print '-----------'
            url = 'http://we.40zhe.com/api/setArticleAttr?id=%s&taobao_id=%s&title=%s' % (item['id'], itemId, title);
            print 'crawl : %s' % url.encode('utf-8')
            rs = requests.get(url)
            print rs.status_code
        except Exception as e:
            url = 'http://we.40zhe.com/api/deleteArticle?id=%s' % item['id'];
            rs = requests.get(url)
            print 'delete %s' % item['id']
            print e
            # print item['taobaoke_url']
            # print driver.page_source

driver.quit()
