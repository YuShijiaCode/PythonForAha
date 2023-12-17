from PythonForAha.Project.Utils.WebCommonStep import WebCommonStep
import time


class WebPage:
    def __init__(self):
        self.common = WebCommonStep()

    def common(self):
        return self.common

    def open_url(self, url):
        self.common.open_url(url)
        time.sleep(1)

