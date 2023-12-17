from PythonForAha.Project.Utils.Driver.Selenium import create_driver
import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class WebCommonStep:
    def __init__(self):
        self.driver = create_driver()

    def open_url(self, url):
        self.driver.get(url)

    def input(self, target_path, text):
        element = self.driver.find_element(By.XPATH, target_path)
        element.clear()
        time.sleep(0.25)
        element.send_keys(text)
        time.sleep(0.25)

    def click(self, target):
        element = self.driver.find_element(By.XPATH, target)
        time.sleep(0.25)
        element.click()

    def wait_until_appeared(self, value, wait_time=20):
        element = WebDriverWait(self.driver, wait_time, poll_frequency=0.2).until(
            EC.presence_of_element_located((By.XPATH, value)),
            message="Wait until timeout: No this element"
        )
        print('text is : ' + element.text)

    def switch_frame(self, frame=None):
        if frame:
            self.driver.switch_to.frame(frame)
        else:
            self.driver.switch_to.default_content()

        time.sleep(0.25)

    def switch_last_window_handle(self):
        window_handles = self.driver.window_handles
        self.driver.switch_to.window(window_handles[-1])
        time.sleep(1)

    def get_title(self):
        self.driver.implicitly_wait(10)
        title = self.driver.title
        print("Title: " + title)
        return title

    def compare_title(self, expect_title):
        actual_title = self.get_title()
        print("Actual title: " + actual_title)
        print("Expected title: " + expect_title)
        assert str(actual_title) == str(expect_title), "Actual title is inconsistent with the expected title"

    def save_screenshot(self, file_name):
        self.driver.save_screenshot(file_name + '.png')

    def save_element_screenshot(self, target_path, file_name):
        element = self.driver.find_element(By.XPATH, target_path)
        element.screenshot(file_name + '.png')
