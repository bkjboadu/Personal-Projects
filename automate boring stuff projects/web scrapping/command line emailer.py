from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests,time

browser = webdriver.Chrome('chromedriver.exe')
browser.get('https://accounts.google.com/signin/v2/identifier?service=mail')

#login_details
login_to_email = browser.find_element_by_name("identifier")
login_to_email.send_keys('brightboadujnr@gmail.com')
login_to_email.send_keys(Keys.ENTER)
time.sleep(5)

#password
password_to_login = browser.find_element_by_name('password')
password_to_login.send_keys('******')
password_to_login.send_keys(Keys.ENTER)
time.sleep(5)

#compose
compose = browser.find_element_by_class_name('z0')
compose.click()
time.sleep(5)

#recipient
recipient = browser.find_element_by_name('to')
recipient.send_keys('brightkjb@gmail.com')

#subject
subject = browser.find_element_by_name('subjectbox')
subject.send_keys('PROGRESS')

#message
subject.send_keys(Keys.TAB)
subject.send_keys('we making a move')
subject.send_keys(Keys.TAB)
subject.send_keys(Keys.ENTER)




