from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Edge('msedgedriver.exe')
browser.get('https://gabrielecirulli.github.io/2048/')
play = browser.find_element_by_tag_name('html')
while True:
    play.send_keys(Keys.ARROW_UP)
    play.send_keys(Keys.ARROW_RIGHT)
    play.send_keys(Keys.ARROW_DOWN)
    play.send_keys(Keys.ARROW_LEFT)