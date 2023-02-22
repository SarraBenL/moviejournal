#!/usr/bin/python
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()

browser.get("http://localhost:5000/")
time.sleep(3)

loginbtn = browser.find_element_by_name('Genre').click();
time.sleep(2)

browser.find_element_by_xpath('//a[@href="'+"/genre?g=35&genre_name=Comedy"+'"]').click();

time.sleep(6)
browser.close()
