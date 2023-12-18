from PythonForAha.Project.PageObject.LoginPage import LoginPage
from PythonForAha.Project.PageObject.HomePage import HomePage
from PythonForAha.Project.PageObject.EditProfilePage import EditProfilePage
from PythonForAha.Project.Utils.WebCommonStep import WebCommonStep
import random


class TestCase_Edit_Profile:
    def testcase_edit_profile(self):
        year = random.randint(1990, 2022)
        month = random.randint(1, 12)
        day = random.randint(1, 29)
        print("----------", str(year) + '-' + str(month) + '-' + str(day))
        common = WebCommonStep()
        login = LoginPage(common)
        home = HomePage(common)
        edit_profile = EditProfilePage(common)
        common.open_url("https://earnaha.com/")
        login.common.wait_until_appeared(login.login_btn(), 50)
        login.click_login_btn()
        login.common.wait_until_appeared(login.username())
        login.input_username("15642543250@163.com")
        login.input_password("Yushijia123+")
        login.click_continue_btn()
        login.common.compare_title("Discover Clubs | Aha | Unlimited Exam Questions")
        home.click_profile_btn()
        edit_profile.click_edit_profile_btn()
        edit_profile.click_birthday()
        edit_profile.select_birthday_in_calendar(str(year) + '-' + str(month) + '-' + str(day))
        edit_profile.click_save_btn()
        edit_profile.compare_birthday('%02d' % day + "/" + '%02d' % month + "/" + str(year)[2:4])
        edit_profile.common.close_browser()