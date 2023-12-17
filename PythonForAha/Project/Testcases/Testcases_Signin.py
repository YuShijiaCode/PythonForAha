from PythonForAha.Project.PageObject.LoginPage import LoginPage


class TestCase_Signin:
    def testcase_sign_in_with_email(self):
        login = LoginPage()
        login.open_url("https://earnaha.com/")
        login.common.wait_until_appeared(login.login_btn(), 50)
        login.click_login_btn()
        login.common.wait_until_appeared(login.username())
        login.input_username("15642543250@163.com")
        login.input_password("Yushijia123+")
        login.click_continue_btn()
        login.common.compare_title("Discover Clubs | Aha | Unlimited Exam Questions")


    def testcase_sign_in_with_google(self):
        login = LoginPage()
        login.open_url("https://earnaha.com/")
        login.common.wait_until_appeared(login.login_btn(), 50)
        login.click_login_btn()
        login.common.wait_until_appeared(login.google_btn())
        login.click_google_btn()
        login.input_google_email("joshuayu1028@gmail.com")
        login.click_google_email_next_step_btn()
        login.common.wait_until_appeared(login.google_password())
        login.input_google_password("yushijia123")
        login.click_google_password_next_step_btn()
        login.common.compare_title("Discover Clubs | Aha | Unlimited Exam Questions")
