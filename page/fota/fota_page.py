# coding = utf8
import os
import sys
from time import sleep

from poco.exceptions import PocoNoSuchNodeException

from page.system.system import System

os.path.abspath(".")
"""
    @File:fota_page.py
    @Author:Bruce
    @Date:2021/1/14
"""


class Fota_Page(System):

    def __init__(self, main_page):
        System.__init__(self, main_page)

        self.guide_page_text = self.poco("com.tcl.fota.system:id/app_guide_title")
        self.guide_continue = self.poco("com.tcl.fota.system:id/guide_continue_button")
        self.download_progress_button = self.poco("com.tcl.fota.system:id/download_progress_button")

    def start_fota_page(self):
        self.logger.info("function:" + sys._getframe().f_code.co_name + ":启动fota app:")
        self.device.start_app(package="com.tcl.fota.system", activity="SystemUpdatesActivity")
        sleep(1)

    def stop_fota_page(self):
        self.logger.info("function:" + sys._getframe().f_code.co_name + ":关闭fota app:")
        sleep(1)
        self.device.stop_app("com.tcl.fota.system")

    def skip_guide(self):
        self.logger.info("function:" + sys._getframe().f_code.co_name + ":跳过设置向导:")
        try:
            if self.guide_page_text.wait().exists():
                self.guide_continue.wait().click()
        except PocoNoSuchNodeException as ex:
            self.logger.warning("function:" + sys._getframe().f_code.co_name +
                                ":无需跳过fota向导界面:" + str(ex))

    def check_new_version(self):
        self.logger.info("function:" + sys._getframe().f_code.co_name + ":检查是否存在最新版本:")
        searching_fota = False
        while not searching_fota:
            self.double_click_element(self.download_progress_button)
            self.download_progress_button.invalidate()
            progress_text = self.download_progress_button.attr("desc")
            print(progress_text)
            if progress_text == "Checking..." or progress_text == "Checking for updates...":
                searching_fota = True
            if searching_fota:
                break
        if self.poco(text="No update available").wait(10).exists():
            self.logger.warning("function:" + sys._getframe().f_code.co_name +
                                ":当前已是最新版本:")
