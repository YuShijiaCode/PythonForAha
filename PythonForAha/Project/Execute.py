import os
import time
import schedule
from PythonForAha.Project.Utils.SendEmail import send_email


# Job that is executed periodically
def job():
    print("Running...")
    # The paths of test files
    execute_path_list = [
        "/Testcases/Testcases_Edit_Profile.py",
        "/Testcases/Testcases_Signin.py",
        "/Testcases/Testcases_SignOut.py"
    ]

    execute_files = ""
    for path in execute_path_list:
        execute_files += os.getcwd() + path + " "

    print(execute_files)
    # execute test files and generate a html report
    os.system("python3 -m pytest " + execute_files + " --html=report.html")
    time.sleep(600)
    # send report to some emails
    send_email("15642543250@163.com", ["1349553285@qq.com"], os.getcwd() + "/report.html")


schedule.every().day.at("09:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
