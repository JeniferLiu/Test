# test_product_info.py
import pytest

from Interface_code01.candao.scripts.A_common.B_utils import get_db_info, get_api_response


@pytest.mark.usefixtures("test_setup")  # Pytest 在执行测试函数之前先执行名为 test_setup 的固件。
class TestProductInfo:

    @pytest.mark.api_test
    @pytest.mark.H
    def test_valid_product_info(self):
        """测试有效的产品信息"""
        product_id = 1
        response = get_api_response(self.base_url, f"products/{product_id}", self.token)
        assert response.status_code == 200

        response_json = response.json()
        sql_result = get_db_info(self.db_utils, f"select id, name from zt_product where id='{product_id}'")
        assert sql_result is not None
        assert response_json['id'] == sql_result['id'] and response_json['name'] == sql_result['name']

    @pytest.mark.api_test
    @pytest.mark.H
    def test_invalid_product_info(self):
        """测试无效的产品信息"""
        product_id = 9999
        response = get_api_response(self.base_url, f"products/{product_id}")
        assert response.status_code == 404

# if __name__ == "__main__":
#     pytest.main(["-vs", __file__, "-m H or M",
#                  "--report=_getproductid_api_1.html",
#                  "--title=candao_接口测试报告",
#                  "--tester=jenifer",
#                  "--template=2"])
