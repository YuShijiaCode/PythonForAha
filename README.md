Project 
  PageObject -> The xpath of element for each page, and some corresponding
    EditProfilePage
    HomePage
    LoginPage
  Testcases
    Testcase_Edit_profile -> 1 cases for edit birthday in edit profile page
    Testcase_Signin   -> Sign in with 2 ways
    TestCase_signout  -> login -> logout
  Utils
    Driver
      Selenium -> generate a driver, so that call api of webdriver to operate
    SendEmail -> The method with SMTP for send email
    WebCommonStep -> some common mothodm include open browser, click, input ...
  Execute -> Set up a scheduler to run the test daily (including weekends) every 9am , and can set the test files
    
