from PythonForAha.Project.PageObject.LoginPage import LoginPage


class TestCase_SignOut:
    def testcase_sign_out(self):
        login = LoginPage()
        login.open_url("https://earnaha.com/")
        login.common.wait_until_appeared(login.login_btn(), 50)
        login.click_login_btn()
        login.common.wait_until_appeared(login.username())
        login.input_username("15642543250@163.com")
        login.input_password("Yushijia123+")
        login.click_continue_btn()
        login.common.compare_title("Discover Clubs | Aha | Unlimited Exam Questions")

