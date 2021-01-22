# coding = utf8
import os
import re
from time import sleep

os.path.abspath(".")

"""
    @File:deskclock_page.py
    @Author:Bruce
    @Date:2021/1/13
"""


class Deskclock_Page:

    # Ui element
    def __init__(self, main_page):
        self.device = main_page.device
        self.poco = main_page.poco
        self.create_clock = self.poco("com.android.deskclock:id/fab")
        self.create_clock_hour = self.poco("com.android.deskclock:id/timerpicker_hour")
        self.create_clock_minute = self.poco("com.android.deskclock:id/timerpicker_minute")
        self.create_clock_save = self.poco("com.android.deskclock:id/toolbar_confirm_btn")

    def start_deskclock(self):
        self.device.start_app("com.android.deskclock")
        sleep(1)

    def stop_deskclock(self):
        sleep(1)
        self.device.stop_app("com.android.deskclock")

    def add_clock(self):
        self.device.start_app("com.android.deskclock")
        self.create_clock.wait().click()
        hour = self.create_clock_hour.wait().attr("desc")
        minute = self.create_clock_minute.wait().attr("desc")
        self.create_clock_save.wait().click()
        hour = re.search("picker (.*)", hour).group(1)
        minute = re.search("picker (.*)", minute).group(1)
        return hour + ":" + minute
