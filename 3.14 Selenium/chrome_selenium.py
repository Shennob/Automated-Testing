import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.set_window_size(1920, 1080)

user_name = driver.find_element(By.ID, "user-name")
user_name.send_keys('standard_user')
print('Input Login')

password = driver.find_element(By.ID, 'password')
password.send_keys("secret_sauce")
print('Input Password')

button_login = driver.find_element(By.ID, 'login-button')
button_login.click()
print('Click Login button')

menu = driver.find_element(By.ID, 'react-burger-menu-btn')
menu.click()

time.sleep(1)

logout_button = driver.find_element(By.ID, 'logout_sidebar_link')
logout_button.click()






