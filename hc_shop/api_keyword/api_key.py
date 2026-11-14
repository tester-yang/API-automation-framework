# coding = utf-8
# Author: Yang
# Date: 2024/3/9 13:43
# 主要定义框架中相关请求,数据提取,数据库连接
import json

import requests
import jsonpath
class api_key():
    # 定义get请求
    def get(self,url, params=None, **kwargs):
        return requests.get(url=url, params=params, **kwargs)
    # 定义post请求
    def post(self,url, data=None, json=None, **kwargs):
        return requests.post(url=url, data=data, json=json, **kwargs)
    # 定义一个json提取器
    def get_text(self,respones,key):
        """
            json.load()从json文件中读取数据
            json.loads()将str类型的数据转换为dict类型
            json.dumps()将dict类型的数据转成str
            json.dump()将数据以json的数据类型写入文件中
        """
        if isinstance(respones,str):
            respones = json.loads(respones)
            res_value = jsonpath.jsonpath(respones,key)
        return res_value[0]

    pass
