#!/usr/bin/python
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()

browser.get("http://localhost:5000/")
time.sleep(3) # Let the user actually see something!

loginbtn = browser.find_element_by_name('login').click();
time.sleep(2)
username = browser.find_element_by_id('InputUsername')
username.send_keys("testuser")
password = browser.find_element_by_id('InputPassword')
password.send_keys("aaaaaa")

password.submit()


time.sleep(5) # Let the user actually see something!
browser.close()
