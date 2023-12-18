import time

# Home page
class HomePage:
    def __init__(self, common_step):
        self.common = common_step
        self._profile_btn = ("//*[@id='__next']/div[2]/div[2]/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div/div/div["
                             "3]/button")
        self._setting_btn = "//*[@href='/profile/settings']"
        self._log_out_btn = "//*[text()='LOG OUT']"
        self._log_out_confirm_btn = "//*[text()='Yes']"
        self._sign_up_btn = "//*[text()='Sign up']"

    def profile_btn(self):
        return self._profile_btn

    def setting_btn(self):
        return self._profile_btn

    def logout_btn(self):
        return self._log_out_btn

    def sign_up_btn(self):
        return self._sign_up_btn

    def click_profile_btn(self):
        self.common.click(self._profile_btn)
        time.sleep(1)

    def click_setting_btn(self):
        self.common.click(self._setting_btn)
        time.sleep(1)

    def click_logout_btn(self):
        self.common.click(self._log_out_btn)
        time.sleep(1)

    def click_logout_confirm_btn(self):
        self.common.click(self._log_out_confirm_btn)
        time.sleep(1)

