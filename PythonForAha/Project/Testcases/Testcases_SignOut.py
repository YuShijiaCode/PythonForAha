from PythonForAha.Project.PageObject.LoginPage import LoginPage
from PythonForAha.Project.PageObject.HomePage import HomePage
from PythonForAha.Project.Utils.WebCommonStep import WebCommonStep


class TestCase_SignOut:
    def testcase_sign_out(self):
        common = WebCommonStep()
        login = LoginPage(common)
        home = HomePage(common)
        common.open_url("https://earnaha.com/")
        common.wait_until_appeared(login.login_btn(), 50)
        login.click_login_btn()
        common.wait_until_appeared(login.username())
        login.input_username("15642543250@163.com")
        login.input_password("Yushijia123+")
        login.click_continue_btn()
        common.compare_title("Discover Clubs | Aha | Unlimited Exam Questions")
        home.click_profile_btn()
        home.click_setting_btn()
        home.click_logout_btn()
        home.click_logout_confirm_btn()
        common.check_element_exist(home.sign_up_btn())
        common.close_browser()
