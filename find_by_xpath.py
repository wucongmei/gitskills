# -*- coding: UTF-8 -*-
from selenium import webdriver
from time import sleep
#拿到driver
driver = webdriver.Firefox()
#跳转网页
driver.get("https://xdclass.net")
print(driver.title)
#睡眠时间3秒
sleep(5)
driver.find_element_by_css_selector(".closed").click()
driver.find_element_by_xpath("/html/body/div/div/div[3]/div/div[2]/a[4]/div/img").click()
print(driver.title)