import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

#  ------------------------------------- TC_001 -------------------------------------- #
driver = webdriver.Chrome(executable_path='./drivers/chromedriver.exe')
driver.maximize_window()
driver.get('https://www.pinterest.com/')

#  ------------------------------------- Log In TC_002 -------------------------------------- #

# TC_2.1 ----------------- #
# login = driver.find_element_by_xpath('//div[@class="tBJ dyH iFc yTZ erh tg7 mWe"]')
# login.click()
# driver.find_element_by_xpath("//input[@id='email']").send_keys('demo@gmail.com')
# driver.find_element_by_xpath("//input[@id='password']").send_keys('123456')
# time.sleep(5)

# TC_2.2 ----------------- #
# login = driver.find_element_by_xpath('//div[@class="tBJ dyH iFc yTZ erh tg7 mWe"]')
# login.click()
# login_fb = driver.find_element_by_xpath("//div[@data-test-id='facebook-connect-button']")
# login_fb.click()
# time.sleep(5)

# TC_2.3 ----------------- #
# login = driver.find_element_by_xpath('//div[@class="tBJ dyH iFc yTZ erh tg7 mWe"]')
# login.click()
# login_google = driver.find_element_by_xpath("//div[@data-test-id='google-connect-button']")
# login_google.click()
# time.sleep(5)



