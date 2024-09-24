import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = 'https://demoqa.com/dynamic-properties'
driver.get(base_url)
driver.set_window_size(1920,1080)

# button_visible = driver.find_element(By.XPATH, "//button[@id='visibleAfter']")
# button_visible.click()

try:
    button_visible = driver.find_element(By.XPATH, "//button[@id='visibleAfter']")
    button_visible.click()
except NoSuchElementException:
    print('Получили NoSuchElementException')
    time.sleep(5)
    driver.refresh()
    time.sleep(5)
    button_visible = driver.find_element(By.XPATH, "//button[@id='visibleAfter']")
    button_visible.click()
    print('Click button visible')






