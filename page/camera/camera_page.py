# coding = utf8
import os
from time import sleep

from page.system.system import System

os.path.abspath(".")
"""
    @File:camera_page.py
    @Author:Bruce
    @Date:2021/1/14
"""

class Camera_Page(System):

    def __init__(self, main_page):
        System.__init__(self, main_page)

        self.top_function_bar = self.poco("com.tcl.camera:id/picker_list_layout")
        self.camera_settings_ai_scene_detection = self.poco(text="AI scene detection")

    def start_camera(self):
        self.device.start_app("com.tcl.camera")
        sleep(1)

    def stop_camera(self):
        sleep(1)
        self.device.stop_app("com.tcl.camera")

    def enter_camera_settings(self):
        self.start_camera()
        camera_settings = self.top_function_bar.wait().children()[0]
        camera_settings.click()
        ai_scene_detection_switch = self.camera_settings_ai_scene_detection.wait().parent().parent().children()[1].children()
        ai_scene_detection_switch.click()
        ai_scene_detection_switch.invalidate()
        switch_status = ai_scene_detection_switch.attr("checked")
        self.stop_camera()
        return switch_status




