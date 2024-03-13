import pytest

from Interface_code01.candao.scripts.A_common.A_auth import get_token
from Interface_code01.candao.scripts.A_common.A_auth import load_config
from Interface_code01.candao.scripts.A_common.db_connection import DataBaseConnection


@pytest.fixture(scope="class")
def test_setup(request):
    """在所有测试用例前执行一次，获取配置和token并建立数据库连接"""
    config_path = 'E:/PycharmProjects/lkxtest1/Interface_code01/candao/scripts/配置文件/dbconfig.json'
    config = load_config(config_path)
    token = get_token(config_path)
    db_utils = DataBaseConnection(config_path)
    base_url = config['api']['base_url']

    request.cls.config = config
    request.cls.token = token
    request.cls.db_utils = db_utils
    request.cls.base_url = base_url
