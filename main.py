import selenium.webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import string
import random

driver = webdriver.Edge()

driver.get('https://id.vnggames.app/register')
time.sleep(2)
continue_button = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/button[1]")
continue_button.click()
time.sleep(2)
# email_txtfield = driver.find_element(By.XPATH,"//input[@placeholder='Nhập email hoặc số điện thoại']")
email_txtfield = driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
email = "example@gmail.com"
email_txtfield.send_keys(email)

time.sleep(2)
checkbox_term = driver.find_element(By.XPATH, "//span[@class='chakra-checkbox__control ecn-css-cache-1sos8ee']")
continue_btn = driver.find_element(By.XPATH, "//button[contains(text(),'Tiếp tục')]")
continue_btn.click()


passwd_txtfield = driver.find_element(By.XPATH, "//input[@placeholder='Mật khẩu']")
password_length = 6
chars = string.ascii_letters + string.digits
passwd_rand = 'PASS'+''.join(random.choice(chars) for i in range(password_length))
passwd_txtfield.send_keys(passwd_rand)
time.sleep(2)
continue_btn = driver.find_element(By.XPATH, "//button[contains(text(),'Tiếp tục')]")
actions = webdriver.ActionChains(driver)
actions.move_to_element(continue_btn)
time.sleep(5)
actions.move_to_element(passwd_txtfield)
time.sleep(30)
driver.quit()