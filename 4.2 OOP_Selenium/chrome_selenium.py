from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

class Test():

    def test_select_product(self):

        driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
        base_url = 'https://www.saucedemo.com/'
        driver.get(base_url)
        driver.set_window_size(1920, 1080)

        print('Start Test')

        user_name = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='user-name']")))
        user_name.send_keys("standard_user")
        print('Input User Name')

        password = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='password']")))
        password.send_keys("secret_sauce")
        print('Input Password')

        button_login = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='login-button']")))
        button_login.click()
        print('Click Login Button')

        select_product = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")))
        select_product.click()
        print('Click Select Product')

        enter_shopping_cart = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@class='shopping_cart_link']")))
        enter_shopping_cart.click()
        print("Enter Shopping Cart")

        success_test = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='title']")))
        value_success_test = success_test.text
        assert value_success_test == 'Your Cart'
        print('Test Success')


start_test = Test()
start_test.test_select_product()









