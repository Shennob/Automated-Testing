from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--headless")

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.set_window_size(1920, 1080)
user_name = driver.find_element(By.ID, "user-name")
user_name.send_keys('standard_user')
print('Input Login')
password = driver.find_element(By.ID, "password")
password.send_keys('secret_sauce')
print('Input Password')
button_login = driver.find_element(By.ID, "login-button")
button_login.click()
print('Click Login Button')
print(driver.current_url)
get_url = driver.current_url
url = 'https://www.saucedemo.com/inventory.html'
assert url == get_url
print('URL корректен')
text_products = driver.find_element(By.XPATH, "//span[@class='title']")
print(text_products.text)
value_text_products = text_products.text
assert value_text_products == 'Products'
print('Заголовок корректен')