from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.set_window_size(1920,1080)

user_name = driver.find_element(By.ID, 'user-name')
user_name.send_keys("standard_user")
print('Input Login')

password = driver.find_element(By.ID, 'password')
password.send_keys("secret_sauce")
print('Input Password')

button_login = driver.find_element(By.ID, 'login-button')
button_login.click()
print('Click Login Button')

product_1 = driver.find_element(By.XPATH, "//*[@id='item_4_title_link']")
value_product_1 = product_1.text
print(value_product_1)

price_product_1 = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[1]/div[2]/div[2]/div")
value_price_product_1 = price_product_1.text
print(value_price_product_1)

select_product_1 = driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-backpack']")
select_product_1.click()
print('Select product 1')

cart = driver.find_element(By.XPATH, "//*[@class='shopping_cart_link']")
cart.click()
print("Enter Cart")

cart_product_1 = driver.find_element(By.XPATH, "//*[@id='item_4_title_link']")
value_cart_product_1 = cart_product_1.text
print(value_cart_product_1)
assert value_product_1 == value_cart_product_1
print("Info Cart Product 1 good")

price_cart_product_1 = driver.find_element(By.XPATH, "//*[@id='cart_contents_container']/div/div[1]/div[3]/div[2]/div[2]/div")
value_cart_price_product_1 = price_cart_product_1.text
print(value_cart_price_product_1)
assert value_price_product_1 == value_cart_price_product_1
print('Info Cart Price Product 1 good')

checkout = driver.find_element(By.XPATH, "//*[@id='checkout']")
checkout.click()
print('Click Checkout')

first_name = driver.find_element(By.XPATH, "//input[@id='first-name']")
first_name.send_keys('Mike')
print('Input First Name')

last_name = driver.find_element(By.XPATH, "//input[@id='last-name']")
last_name.send_keys('Fix')
print('Input Last Name')

postal_code = driver.find_element(By.XPATH, "//input[@id='postal-code']")
postal_code.send_keys(16798)
print('Input Postal Code')

button_continue = driver.find_element(By.XPATH, "//input[@id='continue']")
button_continue.click()
print('Click Continue')

finish_product_1 = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")
value_finish_product_1 = finish_product_1.text
print(value_finish_product_1)
assert value_product_1 == value_finish_product_1
print('Info Finish Product good')

price_finish_product_1 = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[1]/div[3]/div[2]/div[2]/div")
value_finish_price_product_1 = price_finish_product_1.text
print(value_finish_price_product_1)
assert value_price_product_1 == value_finish_price_product_1
print('Info Finish Price Product 1 good')

summary_price = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[2]/div[6]")
value_summary_price = summary_price.text
print(value_summary_price)
item_total = "Item total: " + value_finish_price_product_1
print(item_total)
assert value_summary_price == item_total
print('Total Summary Price good')

button_finish = driver.find_element(By.XPATH, "//*[@id='finish']")
button_finish.click()
print("Enter Button Finish")

checkout_complete = driver.find_element(By.XPATH, "//*[contains(text(), 'Thank you for your order!')]")
value_checkout_complete = checkout_complete.text
print(value_checkout_complete)
assert value_checkout_complete == 'Thank you for your order!'
print('Info Order Complete')























