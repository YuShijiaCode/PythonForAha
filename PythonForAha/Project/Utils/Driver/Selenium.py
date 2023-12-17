from selenium import webdriver


def create_driver():
    option = webdriver.ChromeOptions()
    option.add_argument('--disable-blink-features=AutomationControlled')
    driver = webdriver.Chrome(options=option)
    driver.maximize_window()
    return driver
