# coding = utf8
import csv
import os

from toolsbar.common import logger

os.path.abspath(".")
"""
    @File:save2csv.py
    @Author:Bruce
    @Date:2021/2/20
    @Description:CSV数据的操作库
"""


class Save2Csv:
    # 获取需要保存的数据
    # 写入数据至Excel表格
    # 保存数据格式[x1, x2, x3]
    """
        @description:写入Csv文件
        @param:
            data:写入的数据
            form_name:csv名称
    """

    def writeInCsv(self, data=["Test", "1", "2"], form_name="Fota_Before.csv"):
        with open("./temp/{}".format(form_name), "w", encoding="utf-8-sig") as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(["Case Name", "Previous value", "Set value"])
            # 取出再写入
            for item in data:
                csv_writer.writerow(item)

    """
        @description:读取Csv
        @param:
            form_name:csv名称
    """

    def getDataFromCsv(self, form_name="Fota_Before.csv"):
        csv_list = []
        try:
            with open("./temp/{}".format(form_name), "r", encoding="utf-8-sig") as csv_file:
                csv_reader = csv.reader(csv_file)
                next(csv_reader)
                for item in csv_reader:
                    csv_list.append(item)
        except FileNotFoundError:
            logger.error("{} 不存在,请检查!".format(form_name))

        return csv_list
