import json

import requests


def load_config(config_path):
    """加载配置文件"""
    with open(config_path, 'r') as f:
        return json.load(f)


def get_header(token):
    """获取请求头"""
    return {"Token": token, "Content-Type": "application/json"}


def get_db_info(db_utils, query_sql):
    """从数据库获取信息"""
    try:
        query_result = db_utils.execute_query(query_sql)
        return query_result[0] if query_result else None
    except Exception as e:
        print(f"数据库查询失败: {e}")
        return None


def delete_db_info(db_utils, delete_sql):
    """删除测试数据"""
    try:
        delete_result = db_utils.execute_dml(delete_sql)
        if delete_result:
            print("测试数据已成功删除")
        else:
            print("没有找到要删除的测试数据")
    except Exception as e:
        print(f"删除数据库信息失败: {e}")


def get_api_response(base_url, endpoint, token=None):
    """发送GET API请求并获取响应"""
    url = f"{base_url}/{endpoint}"
    headers = get_header(token) if token else {"Content-Type": "application/json"}
    response = requests.get(url=url, headers=headers)
    return response


def put_api_response(base_url, endpoint, data, token=None, headers=None):
    """发送PUT API请求并获取响应"""
    url = f"{base_url}/{endpoint}"
    request_headers = get_header(token) if token else {"Content-Type": "application/json"}
    if headers:
        request_headers.update(headers)
    if not isinstance(data, str):
        data = json.dumps(data)
    response = requests.put(url=url, headers=request_headers, data=data)
    return response


def post_api_response(base_url, endpoint, data, token=None, headers=None):
    """发送POST API请求并获取响应"""
    url = f"{base_url}/{endpoint}"
    request_headers = get_header(token) if token else {"Content-Type": "application/json"}
    if headers:
        request_headers.update(headers)
    if not isinstance(data, str):
        data = json.dumps(data)
    response = requests.post(url=url, headers=request_headers, data=data)
    return response


def delete_api_response(base_url, endpoint, token=None, headers=None):
    """发送delete API 请求并获取响应"""
    url = f"{base_url}/{endpoint}"
    request_headers = get_header(token) if token else {"Content-Type": "application/json"}
    if headers:
        request_headers.update(headers)
    response = requests.delete(url=url, headers=request_headers)
    return response
