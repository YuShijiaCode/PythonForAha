from selenium.common import NoSuchElementException

from PythonForAha.Project.Utils.Driver.Selenium import create_driver
import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class WebCommonStep:
    def __init__(self):
        self.driver = create_driver()

    def create_driver(self):
        self.driver = create_driver()
        return self.driver

    def close_browser(self):
        self.driver.quit()
        time.sleep(5)

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

    def get_text(self, target_xpath):
        text = self.driver.find_element(By.XPATH, target_xpath).text
        print("Text: " + text)
        return text

    def get_attribute(self, target_xpath, attr='value'):
        attr_value = self.driver.find_element(By.XPATH, target_xpath).get_attribute(attr)
        print("Attribute_Value: " + attr_value)
        return attr_value

    def compare_title(self, expect_title):
        actual_title = self.get_title()
        print("Actual title: " + actual_title)
        print("Expected title: " + expect_title)
        assert str(actual_title) == str(expect_title), "Actual title is inconsistent with the expected title"

    def compare_text(self, expect_text, target_xpath):
        actual_text = self.get_text(target_xpath)
        print("Actual Text: " + actual_text)
        print("Expected Text: " + expect_text)
        assert str(actual_text) == str(expect_text), "Actual text is inconsistent with the expected text"

    def save_screenshot(self, file_name):
        self.driver.save_screenshot(file_name + '.png')

    def save_element_screenshot(self, target_path, file_name):
        element = self.driver.find_element(By.XPATH, target_path)
        element.screenshot(file_name + '.png')

    def check_element_exist(self, target):
        try:
            element = self.driver.find_element(By.XPATH, target)
            print("Element exists: " + element.text)
        except NoSuchElementException:
            assert False, "Element is not exist!"

    def input_date_in_calendar(self, target_xpath, date):
        js = 'document.evaluate("' + target_xpath + '",document).iterateNext().removeAttribute("readonly")'
        self.driver.execute_script(js)
        time.sleep(1)
        js_value = 'document.evaluate("' + target_xpath + '",document).iterateNext().value="'+date+'"'
        self.driver.execute_script(js_value)
        time.sleep(100)
