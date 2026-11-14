# coding = utf-8
# Author: Yang
# Date: 2024/3/9 13:50
import json

from hc_shop.common.FileDataDriver import *
from hc_shop.api_keyword.api_key import api_key
import pytest


class TestCase():
    # 读取excel文件
    excel_data = FileReader.read_excel()

    # print(excel_data)
    # 定义关键字
    def setup_method(self):
        self.ak = api_key()

    # 定义一个内置函数,用来提取接口返回的值
    def __jsonpath(self, excel_value, response):
        try:
            pass
        except Exception as e:
            pass

    # 使用pytest中的parametrize方法来循环获取excel中的数据
    @pytest.mark.parametrize("excel_value", excel_data)
    def test01(self, excel_value):
        row = excel_value["id"]
        column = 12
        try:
            # 1.接口参数
            # url
            url = excel_value["url"]
            # path
            path = excel_value["path"]
            # print(excel_value)
            # method
            method = excel_value["method"]
            # params
            params = eval(excel_value["params"])
            # print(params)
            # headers
            headers = eval(excel_value["headers"])
            # data
            if excel_value["data"] is None:
                data = None
            else:
                data = eval(excel_value["data"])
                print(data)
                # json_data = json.loads(excel_value["data"])
            dict_data = {
                "url": url + path,
                "params": params,
                # "headers": headers,
                "data": data
            }
        except Exception as e:
            print("未获取到对应的请求参数值", e)
            FileReader.write_excel(row=row, column=column, value="未获取到对应的请求参数值")

        # 使用反射函数来获取api_key中的请求方法
        else:
            response = getattr(self.ak, method)(**dict_data)
            # 使用json提取器来提取接口返回内容
            try:
                # if excel_value["actualResult"] and excel_value["expectResult"]:
                actualResult = excel_value["actualResult"]
                expectResult = excel_value["expectResult"]
                # print(f"actualResult:{actualResult},expectResult:{expectResult}")
                msg = self.ak.get_text(response.text, actualResult)
                print(f"预期值:{expectResult},实际值:{msg}")
            except Exception as e:
                print("案例excel中缺少actualResult或expectResult字段", e)
                FileReader.write_excel(row=row, column=column, value="案例excel中缺少actualResult或expectResult字段")
            else:
                # msg接口返回值与实际结果比较
                if expectResult == msg:
                    result_value = "执行通过"
                else:
                    result_value = "执行失败"
                FileReader.write_excel(row=row, column=column, value=result_value)

            pass