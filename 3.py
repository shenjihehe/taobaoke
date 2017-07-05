#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import time
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
try:
    driver.set_window_size(480, 800)
    driver.get('https://daren.taobao.com/account_page/daren_home.htm?ut_sk=1.WPI25dtUaBgDAJf6gmZ5TzlT_21380790_1498295193754.TaoPassword-QQ.4&wh_weex=true&sourceType=other&user_id=1952388730&_fromTBWebVC=1&spm=a21r6.8160677.Author.d1&suid=8CBE588C-5021-4E6B-A957-3816D3E07199&cpp=1&shareurl=true&short_name=h.9byeV6&cv=DPbhZyORgXW&sm=bf5bf4&app=chrome')
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
                url = 'http://article.app/api/writeGoods?title=%s&des=%s&img_src=%s&price=%s&taobaoke_url=%s' % (title, des, image_src, price, taobaoke_url)
                print 'simple goods crawl : %s' % url.encode('utf-8')
                rs = requests.get(url)
                print rs.status_code
            except Exception as e:
                continue
    except Exception as e:
        print e
except Exception as e:
    print e

driver.quit()
