import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = 'https://lambdatest.com/selenium-playground/simple-form-demo'
driver.get(base_url)
driver.set_window_size(1920,1080)

first_value = 123
second_value = 101
sum_result = first_value + second_value

input_first_value = driver.find_element(By.XPATH, "//input[@id='sum1']")
input_first_value.send_keys(first_value)

input_second_value = driver.find_element(By.XPATH, "//input[@id='sum2']")
input_second_value.send_keys(second_value)

click_button = driver.find_element(By.XPATH, "//*[@id='gettotal']/button")
click_button.click()

time.sleep(3)

result = driver.find_element(By.XPATH, "//p[@id='addmessage']")
value_result = result.text
assert value_result == str(sum_result)
print('Значения равны')


