#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import time
import requests
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

while True:
    driver = webdriver.Chrome()
    try:
        print 'simple goods'
        r = requests.get('http://we.40zhe.com/api/getTkAuthors')
        if (r.status_code != 200):
            time.sleep(2)
            continue

        obj = json.loads(r.text, encoding='utf-8')
        if (len(obj) == 0):
            time.sleep(2)
            continue

        print obj
        for item in obj:
            driver.set_window_size(480, 800)
            driver.get(item['url'])
            driver.find_element_by_tag_name('body').click()
            for i in range(0, 20):
                driver.find_element_by_tag_name('body').send_keys(Keys.END)
                time.sleep(1)

            try:
                for item in range(0, 120):
                    try:
                        price = driver.find_element_by_xpath('//*[@id="rx-block"]/div/div[%d]/div/div/a/div/div[2]/span' % item).text
                        des = driver.find_element_by_xpath('//*[@id="rx-block"]/div/div[%d]/div/div/div/a/span[2]' % item).text
                        taobaoke_url = driver.find_element_by_xpath('//*[@id="rx-block"]/div/div[%d]/div/div/div/a' % item).get_attribute('href')

                        driver2 = webdriver.Chrome()
                        driver2.get(taobaoke_url)
                        real_url = driver2.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[2]/a').get_attribute('href')
                        image_src = driver2.find_element_by_xpath('//*[@id="scroll"]/div/div[1]/div/a/div[1]/div[1]/div/div/div[1]/div/img').get_attribute('src')
                        driver2.quit()

                        print '---------------'
                        print des
                        print price[1:]
                        print taobaoke_url
                        print image_src
                        print '---------------'
                        rs = requests.post(url='http://we.40zhe.com/api/writeGoods', data={
                            'price': price[1:],
                            'des': des,
                            'taobaoke_url': real_url,
                            'img_src': image_src
                        }, timeout = 3)
                        print rs.url
                        print rs.status_code
                        print rs.text
                    except Exception as e:
                        print e
                        continue
            except Exception as e:
                print e
                continue
    except Exception as e:
        print e

    print 'quit'
    driver.quit()
    print 'sleep'
    time.sleep(300)



