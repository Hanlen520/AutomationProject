# coding = utf8

import os
import re
import subprocess

os.path.abspath(".")

"""
    @File:config.py
    @Author:Bruce
    @Date:2020/12/15
    @Description:配置库，对设备进行操作
"""

# ['7c2440fd', 'b3e5b958']
"""
    @description:获取设备序列号
"""


def get_serial_number():
    devices_stream = os.popen("adb devices")
    devices = devices_stream.read()
    serial_no = re.findall("(.*)\tdevice", devices)
    devices_stream.close()
    return serial_no


# 测试前安装所需APP
"""
    @description:安装app至设备中
    @param:
        device:设备
"""


def install_app_necessary(device=""):
    files = subprocess.Popen("ls ./apk/", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
    apks = [i for i in re.split(",", str(files).strip("b'").replace("\\n", ",")) if i != ""]
    print(apks)
    # 如下置灰代码用于独立出来不借助poco，独立使用python代码
    # for device_serial in SERIAL_NUMBER:
    #     for apk in apks:
    #         print("Device [{}] is install {}".format(device_serial, apk))
    #         screenData = subprocess.Popen("adb -s {} install ./apk/{}.apk".format(device_serial, apk),
    #                                       stdout=subprocess.PIPE, shell=True)
    #         while True:
    #             line = screenData.stdout.readline()
    #             print(line.decode("utf-8"))
    #             if line == b"" or subprocess.Popen.poll(screenData) == 0:
    #                 screenData.stdout.close()
    #                 break
    for apk in apks:
        print("Device [{}] is install {}".format(device.serialno, apk))
        install_result = device.install_app("./apk/" + apk)
        print(install_result)


# Return devices serial number
"""
    @description:获取当前连接的所有设备序列号
"""
SERIAL_NUMBER = get_serial_number()
