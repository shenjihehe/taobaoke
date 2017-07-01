import requests
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("httpsss://i.click.taobao.com/t?e=m%3D2%26s%3DdQmBsP8rj9dw4vFB6t2Z2ueEDrYVVa646og1Ii54c8gYX8TY%2BNEwdxGhNfJpcvprLzKPa%2Ff2nu%2BONcmTXFDqVFUUeSyuzvzndwuIdUvuKnQgWIMF8jh8TT%2BYs7%2Fl%2BgH1ARvmImZc5Rf68BkhUpufuNREFoJ0Y68HrlXo0jK5P0Z1BxIwYavbk6Jn5AyUbPoV&pg1stepk=ucm:200272793029_174316785_%7B%22common_content_page%22:darenhome%7D")
ele = driver.find_element_by_name("item_id")
print ele.get_attribute("value")
