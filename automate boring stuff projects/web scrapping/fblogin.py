from selenium import webdriver
browser = webdriver.Chrome('chromedriver.exe')
browser.get('https://web.facebook.com/')
User_elem = browser.find_element_by_id('email')
User_elem.send_keys('0242753604')
Pass_elem = browser.find_element_by_id('pass')
Pass_elem.send_keys('*******')
login_elem = browser.find_element_by_name('login')
login_elem.click()
