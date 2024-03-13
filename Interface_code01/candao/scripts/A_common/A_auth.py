# A_auth.py
import json

import requests

from Interface_code01.candao.scripts.A_common.B_utils import load_config


def get_token(config_path):
    """获取 token信息"""
    config = load_config(config_path)
    auth = config['api']['auth']
    print(auth)
    try:
        url = f"{config['api']['base_url']}/tokens"
        print(url)
        response = requests.post(url, json=auth)

        if response.status_code == 201:
            return response.json().get('token')
        else:
            print(f"获取token失败，状态码：{response.status_code}, 响应内容：{json.loads(response.text)}")
    except Exception as e:
        print("请求token时发生错误：", e)


if __name__ == '__main__':
    token = get_token("E:\PycharmProjects\lkxtest1\Interface_code01\candao\scripts\配置文件\dbconfig.json")
    print(f"获取到的token: {token}")
