import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = 'https://lambdatest.com/selenium-playground/jquery-dropdown-search-demo'
driver.get(base_url)
driver.set_window_size(1920,1080)

click_drop = driver.find_element(By.XPATH, "//span[@aria-labelledby='select2-country-container']")
click_drop.click()

time.sleep(1)

select_country = driver.find_element(By.XPATH, ("//li[@class='select2-results__option'])[3]"))
select_country.click()

