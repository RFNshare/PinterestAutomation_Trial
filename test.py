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

# TC_2.1 Login by email----------------- #
login = driver.find_element_by_xpath('//div[@class="tBJ dyH iFc yTZ erh tg7 mWe"]')
login.click()
driver.find_element_by_xpath("//input[@id='email']").send_keys('demo@gmail.com')
driver.find_element_by_xpath("//input[@id='password']").send_keys('123456')
time.sleep(5)
driver.find_element_by_xpath("//div[@data-test-id='registerFormSubmitButton']").click()

# TC_2.2 Login by Facebook----------------- #
# login = driver.find_element_by_xpath('//div[@class="tBJ dyH iFc yTZ erh tg7 mWe"]')
# login.click()
# login_fb = driver.find_element_by_xpath("//div[@data-test-id='facebook-connect-button']")
# login_fb.click()
# time.sleep(5)

# TC_2.3 Login by Google----------------- # Problem***
# login = driver.find_element_by_xpath('//div[@class="tBJ dyH iFc yTZ erh tg7 mWe"]')
# login.click()
# login_google = driver.find_element_by_xpath("//div[@data-test-id='google-connect-button']")
# login_google.click()
# time.sleep(5)


#  ------------------------------------- Sign Up TC_003 -------------------------------------- #
# TC_3.1 Signup with email----------------- #
# sign_up = driver.find_element_by_xpath(
#     '//div[@class="tBJ dyH iFc yTZ pBj tg7 mWe"]')
# sign_up.click()
# email_field = driver.find_element_by_xpath("//input[@id='email']")
# time.sleep(3)
# email_field.send_keys("af.qups@gmail.com")
# time.sleep(3)
# pass_filed = driver.find_element_by_xpath("//input[@id='password']")
# time.sleep(3)
# pass_filed.send_keys("asdfgh.123")
# time.sleep(3)
# age_filed = driver.find_element_by_xpath("//input[@id='age']")
# time.sleep(3)
# age_filed.send_keys("25")
# time.sleep(3)
# driver.find_element_by_xpath("//div[text()='Continue']").click()
# time.sleep(5)
# driver.quit()

# TC_3.2 Signup by Facebook----------------- #
# main_page = driver.current_window_handle
# login = driver.find_element_by_xpath('//div[@class="tBJ dyH iFc yTZ erh tg7 mWe"]')
# login.click()
# login_fb = driver.find_element_by_xpath("//div[@data-test-id='facebook-connect-button']")
# login_fb.click()
# time.sleep(5)
# for handle in driver.window_handles:
#     if handle != main_page:
#         fb_login = handle
# driver.switch_to.window(fb_login)
# fb_email = driver.find_element_by_xpath("//input[@id='email']")
# fb_email.send_keys("af.qups@gmail.com")
# fb_pass = driver.find_element_by_xpath("//input[@id='pass']")
# fb_pass.send_keys("asdfgh123")
# fb_submit = driver.find_element_by_xpath("//input[@name='login']")
# fb_submit.click()


# TC_2.3 Signup by Google----------------- # Problem***
# login = driver.find_element_by_xpath('//div[@class="tBJ dyH iFc yTZ erh tg7 mWe"]')
# login.click()
# # login_google = driver.find_element_by_xpath("//div[@class='zI7 iyn Hsu']")
# # print(login_google.text)
# wait = WebDriverWait(driver, 10)
# wait.until(EC.presence_of_element_located((By.XPATH, "//div[@data-test-id='google-connect-button']")))
# a = driver.find_element_by_xpath("//div[@data-test-id='google-connect-button']")
# a.click()
# time.sleep(5)

#  ------------------------------------- Homepage TC_004 -------------------------------------- #
# TC_4.1 LOGO----------------- #
# logo = driver.find_element_by_xpath("//div[@data-test-id='pinterest-logo']")
# logo.click()
