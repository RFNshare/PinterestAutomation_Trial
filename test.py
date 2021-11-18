import time

from selenium import webdriver

# TC_001 --------------------------- #
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path='./drivers/chromedriver.exe')
driver.maximize_window()
driver.get('https://www.pinterest.com/')

# TC_002 --------------------------- #

# TC_002.1 ----------------- #
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="tBJ dyH iFc yTZ erh tg7 mWe"]')))
login_email = driver.find_element_by_xpath('//div[@class="tBJ dyH iFc yTZ erh tg7 mWe"]')
login_email.click()
driver.find_element_by_xpath("//input[@id='email']").send_keys('demo@gmail.com')
driver.find_element_by_xpath("//input[@id='password']").send_keys('123456')
time.sleep(5)
driver.quit()
