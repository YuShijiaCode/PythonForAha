import time


# Edit Profile Page
class EditProfilePage:
    def __init__(self, common_step):
        self.common = common_step
        # xpath for element
        self._edit_profile_btn = "//*[text()='Edit Profile']"
        self._birthday_input = "//*[@name='birthday']"
        self._save_btn = "//*[text()='Save']"
        self._pick_year = "//*[@title='Pick year']"
        self._previous_month = "//*[@title='Previous month']"
        self._next_month = "//*[@title='Next month']"
        self._ok_btn = "//*[text()='OK']"

    def edit_profile_btn(self):
        return self._edit_profile_btn

    def birthday(self):
        return self._birthday_input

    def save_btn(self):
        return self._save_btn

    def click_edit_profile_btn(self):
        self.common.click(self._edit_profile_btn)
        time.sleep(5)

    def click_save_btn(self):
        self.common.click(self._save_btn)
        time.sleep(1)

    def click_birthday(self):
        self.common.click(self._birthday_input)
        time.sleep(1)

    def select_birthday_in_calendar(self, date):
        year, month_number, day = date.split("-")[0], date.split("-")[1], date.split("-")[2]
        month_name = ["January", "February", "March", "April", "May", "June", "July",
                      "August", "September", "October", "November", "December"]
        month = month_name[int(month_number) - 1]
        self.common.click(self._pick_year)
        time.sleep(1)
        self.common.click("//*[@data-year='" + year + "']")
        time.sleep(1)
        for i in range(13):
            month_year = self.common.get_text(self._pick_year)
            default_month = month_year.split(" ")[0]
            if month == default_month:
                break
            else:
                self.common.click(self._next_month)
        time.sleep(1)
        default_year = self.common.get_text(self._pick_year).split(" ")[1]
        if default_year != year:
            for i in range(12):
                self.common.click(self._previous_month)
        self.common.click("//*[@class='MuiButtonBase-root css-11duv1i' and text()='" + day + "']")
        time.sleep(1)
        self.common.click(self._ok_btn)
        time.sleep(1)

    def compare_birthday(self, expected_value):
        actual_value = self.common.get_attribute(self._birthday_input)
        print("Actual value: " + actual_value)
        print("Expected value: " + expected_value)
        assert str(actual_value) == str(expected_value), "Actual value is inconsistent with the expected value"
