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
from selenium.webdriver.common.keys import Keys

while True:
    try:
        print 'talent simple goods'
        r = requests.get('http://we.40zhe.com/api/getTkAuthors')
        if (r.status_code != 200):
            time.sleep(2)
            continue

        obj = json.loads(r.text, encoding='utf-8')
        if (len(obj) == 0):
            time.sleep(2)
            continue

        for item in obj:
            driver = webdriver.Chrome()
            driver.set_window_size(480, 800)
            driver.get(item['url'])
            driver.find_element_by_tag_name('body').click()
            for i in range(0, 40):
                driver.find_element_by_tag_name('body').send_keys(Keys.END)
                time.sleep(1)

            try:
                for item in range(0, 120):
                    try:
                        real_url = ''
                        image_src = ''

                        price = driver.find_element_by_xpath(
                            '//*[@id="rx-block"]/div/div[%d]/div/div/a/div/div[3]/span' % item).text
                        des = driver.find_element_by_xpath(
                            '//*[@id="rx-block"]/div/div[%d]/div/div/div/a/span[2]' % item).text
                        taobaoke_url = driver.find_element_by_xpath(
                            '//*[@id="rx-block"]/div/div[%d]/div/div/div/a' % item).get_attribute('href')

                        if taobaoke_url:
                            print 'taobaoke-url'
                            driver2 = webdriver.Chrome()
                            driver2.get(taobaoke_url)
                            try:
                                real_url = driver2.find_element_by_xpath(
                                    '//*[@id="rx-block"]/div/div[2]/div/div/div[2]').get_attribute('data-spm-d')
                            except:
                                pass
                            driver2.quit()

                        print '---------------'
                        print des
                        print price[1:]
                        print real_url[1:]
                        rs = requests.post(url='http://we.40zhe.com/api/writeGoods', data={
                            'price': price[1:],
                            'des': des,
                            'taobaoke_url': real_url[1:],
                            'img_src': ''
                        }, timeout=10)
                        print rs.url
                        print rs.status_code
                        print rs.text
                        print '---------------'
                    except Exception as e:
                        print '-1-'
                        print e
                        print '-1-'
                        continue
            except Exception as e:
                print '-2-'
                print e
                print '-2-'
                driver.quit()
                continue

            driver.quit()


    except Exception as e:
        print '-3-'
        print e
        print '-3-'

    rand = random.randint(10, 20)
    print 'sleep : %s' % rand
    time.sleep(rand)
