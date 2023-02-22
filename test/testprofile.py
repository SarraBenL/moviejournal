#!/usr/bin/python
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()

browser.get("http://localhost:5000/")
time.sleep(3)

loginbtn = browser.find_element_by_name('login').click();
time.sleep(2)
username = browser.find_element_by_id('InputUsername')
username.send_keys("testuser")
password = browser.find_element_by_id('InputPassword')
password.send_keys("aaaaaa")
password.submit()

time.sleep(5)
browser.find_element_by_xpath("//a[@href='#reviews']").click();

time.sleep(5)
browser.find_element_by_xpath("//a[@href='#watchlist']").click();

time.sleep(5)
browser.find_element_by_xpath("//a[@href='#lists']").click();

time.sleep(5)

editbtn = browser.find_element_by_name('editprofile').click();
time.sleep(2)
username = browser.find_element_by_id('exampleInputUsername1')
username.send_keys("testuser")
email = browser.find_element_by_id('exampleInputEmail1')
email.send_keys("nedaz503@gmail.com")
password1 = browser.find_element_by_id('exampleInputPassword1')
password1.send_keys("aaaaaa")
password2 = browser.find_element_by_id('exampleInputPassword2')
password2.send_keys("aaaaaa")


browser.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[1]/div/div/form/div[3]/button[2]").click();

time.sleep(6)


browser.close()
