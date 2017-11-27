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

try:
    print 'talent simple goods'
    r = requests.get('http://we.40zhe.com/api/getTkAuthors')
    obj = json.loads(r.text, encoding='utf-8')

    for data in obj:
        driver = webdriver.Chrome()
        driver.set_window_size(480, 800)
        driver.get(data['url'])
        driver.find_element_by_tag_name('body').click()
        for i in range(0, 40):
            driver.find_element_by_tag_name('body').send_keys(Keys.END)
            time.sleep(1)
#       
        index = 0
        for item in range(0, 120):
            try:
                taobaoke_url = driver.find_element_by_xpath(
                    '//*[@id="rx-block"]/div/div[%s]/div/div/div[1]/a[3]' % item).get_attribute('href')

                print '-------------'
                print item
                print taobaoke_url
                print '-------------'

                try:
                    driver2 = webdriver.Chrome()
                    driver2.get(taobaoke_url)
                    divs = driver2.find_elements_by_xpath('//*[@id="rx-block"]/div/div[@data-spm="richtext"]')
                    arr = []
                    index = 0
                    for item in divs:
                        try:
                            div = item.find_element_by_xpath('div/div/div')
                            taobao = div.find_element_by_xpath('a').get_attribute('href')
                            price = div.find_element_by_xpath('a/div/div[2]/span[1]').get_attribute('innerHTML')
                            rs = requests.post(url='http://we.40zhe.com/api/writeGoods', data={
                                'price': price[1:],
                                'des': divs[index + 1].text,
                                'taobaoke_url': taobao,
                                'img_src': ''
                            }, timeout=10)
                            index+=1

                            print '-------------'
                            print taobao
                            print price[1:]
                            print divs[index + 1].text
                            print rs.status_code
                            print rs.text
                            print '---------------'
                            # src = div.find_element_by_xpath('a/div/div[1]/img').get_attribute('src')
                            # arr.append({'taobaokeUrl': taobao, 'imgSrc': src, 'des': divs[index + 1].text, 'price': price[1:]})
                        except Exception as e:
                            print '--------item'
                            print e
                            print '--------'
                            index+=1
                            continue
                except Exception as e:
                    print 'driver2 quit'
                    print e
                    driver2.quit()
                    continue
            except Exception as e:
                print '-1-'
                print e
                print '-1-'
                continue
#
#         driver.quit()
#
#
except Exception as e:
    print '-3-'
    print e
    print '-3-'
