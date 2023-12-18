import time


class LoginPage:
    def __init__(self, common_step):
        self.common = common_step
        self._login_btn = "(//*[@class='h1-button-container'])[1]"
        self._username = "//*[@id='username']"
        self._password = "//*[@id='password']"
        self._continue_btn = "/html/body/div[1]/main/section/div/div/div/form/div[3]/button"
        self._google_btn = "//*[@data-provider='google']"
        self._google_email = "//*[@id='identifierId']"
        self._google_email_next_btn = "//*[@id='identifierNext']/div/button"
        self._google_password = "//*[@name='Passwd']"
        self._google_password_next_btn = "//*[@id='passwordNext']/div/button"


    def login_btn(self):
        return self._login_btn

    def username(self):
        return self._username

    def password(self):
        return self._password

    def continue_btn(self):
        return self._continue_btn

    def google_btn(self):
        return self._google_btn

    def google_email(self):
        return self._google_email

    def google_password(self):
        return self._google_password

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

    def click_google_btn(self):
        self.common.click(self._google_btn)
        time.sleep(1)

    def input_google_email(self, text):
        self.common.input(self._google_email, text)
        time.sleep(1)

    def click_google_email_next_step_btn(self):
        self.common.click(self._google_email_next_btn)
        time.sleep(3)

    def input_google_password(self, text):
        self.common.input(self._google_password, text)
        time.sleep(1)

    def click_google_password_next_step_btn(self):
        self.common.click(self._google_password_next_btn)
        time.sleep(3)
