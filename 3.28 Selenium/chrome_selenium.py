from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = 'https://www.lambdatest.com/selenium-playgroud/upload-file-demo'
driver.get(base_url)
driver.set_window_size(1920,1080)

path_upload = "C:\\Users\\имя_пользователя\\PycharmProjects\\дериктория_проекта\\дериктория_файлов\\screenshot.png"

click_button = driver.find_element(By.XPATH, "//input[@id='file']")
click_button.send_keys(path_upload)









