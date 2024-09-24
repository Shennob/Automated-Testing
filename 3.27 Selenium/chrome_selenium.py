import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = 'https://the-internet.herokapp.com/javascript_alerts'
driver.get(base_url)
driver.set_window_size(1920,1080)

click_alert_button = driver.find_element(By.XPATH, "//button[@onclick='jsAlert()']")
click_alert_button.click()
print('Click Alert Button')
time.sleep(3)
driver.switch_to.alert.accept()

click_alert_button = driver.find_element(By.XPATH, "//button[@onclick='jsConfirm()']")
click_alert_button.click()
print('Click Alert Button')
time.sleep(3)
driver.switch_to.alert.dismiss()

click_alert_button = driver.find_element(By.XPATH, "//button[@onclick='jsPrompt()']")
click_alert_button.click()
print('Click Alert Button')
time.sleep(3)
driver.switch_to.alert.send_keys('Hello')
driver.switch_to.alert.accept()










