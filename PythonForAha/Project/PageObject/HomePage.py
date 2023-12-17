from PythonForAha.Project.PageObject.WebPage import WebPage
import time
from PythonForAha.Project.Utils.Driver.Selenium import create_driver
from PythonForAha.Project.Utils.WebCommonStep import WebCommonStep


class HomePage(WebPage):
    def __init__(self):
        super().__init__()

        # self._login_btn = "//*[Text='Log In']"

        self._login_btn = "(//*[@class='h1-button-container'])[1]"
        self._username = "//*[@id='username']"
        self._password = "//*[@id='password']"
        self._continue_btn = "/html/body/div[1]/main/section/div/div/div/form/div[3]/button"

    def login_btn(self):
        return self._login_btn

    def username(self):
        return self._username

    def password(self):
        return self._password

    def continue_btn(self):
        return self._continue_btn

    def click_login_btn(self):
        self.common.click(self._login_btn)

    def input_username(self, text):
        self.common.input(self._username, text)
        time.sleep(1)

    def input_password(self, text):
        self.common.input(self._password, text)
        time.sleep(1)

    def click_continue_btn(self):
        self.common.click(self._continue_btn)
        time.sleep(1)

