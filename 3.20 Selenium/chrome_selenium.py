import time
from datetime import datetime

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = 'https://demoqa.com/data-picker'
driver.get(base_url)
driver.set_window_size(1920,1080)

date_input = driver.find_element(By.XPATH, "//input[@id='datePickerMonthYearInput']")
date_input.send_keys(Keys.CONTROL + 'a')
date_input.send_keys(Keys.DELETE)

time.sleep(1)

current_date = datetime.now().strftime("%d.%m.%Y")
date_input.send_keys(current_date)