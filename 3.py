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
            time.sleep(300)
            continue

        obj = json.loads(r.text, encoding='utf-8')
        if (len(obj) == 0):
            time.sleep(300)
            continue

        print obj
        for item in obj:
            driver.set_window_size(480, 800)
            driver.get(item['url'])
            driver.find_element_by_tag_name('body').click()
            for i in range(0, 15):
                driver.find_element_by_tag_name('body').send_keys(Keys.END)
                time.sleep(2)

            try:
                for item in range(0, 120):
                    try:
                        price = driver.find_element_by_xpath('//*[@id="rx-block"]/div/div[%d]/div/div/a/div/div[2]/span' % item).text
                        title = driver.find_element_by_xpath('//*[@id="rx-block"]/div/div[%d]/div/div/div/a/span[1]' % item).text
                        des = driver.find_element_by_xpath('//*[@id="rx-block"]/div/div[%d]/div/div/div/a/span[2]' % item).text
                        taobaoke_url = driver.find_element_by_xpath('//*[@id="rx-block"]/div/div[%d]/div/div/div/a' % item).get_attribute('href')
                        img_src = driver.find_element_by_xpath('//*[@id="rx-block"]/div/div[%d]/div/div/a/div/div[1]' % item)

                        image_src = img_src.value_of_css_property('background-image').replace('url("', '').replace('"', '').replace(')', '').replace('(', '')
                        rs = requests.get(url='http://we.40zhe.com/api/writeGoods', params={
                            'price': price,
                            'title': title,
                            'des': des,
                            'taobaoke_url': taobaoke_url,
                            'img_src': img_src
                        })
                        print rs.url
                        print rs.status_code
                        print rs.text
                    except Exception as e:
                        continue
            except Exception as e:
                print e
    except Exception as e:
        print e

    driver.quit()
    time.sleep(300)



