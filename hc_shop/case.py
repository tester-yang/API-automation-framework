# coding = utf-8
# Author: Yang
# Date: 2024/3/6 23:12
import requests

url = "http://shop-xo.hctestedu.com?s=/api/user/login"
headers = {"Content-Type": "application/json"}
params = {"application": "app",
          "application_client_type": "pc"}
data = {"accounts": "ceshitest", "pwd": "123456", "type": "username"}
response = requests.post(url=url, headers=headers, params=params, json=data)
print(response.json())
