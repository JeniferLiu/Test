import pytest

from Interface_code01.candao.scripts.A_common.B_utils import put_api_response, get_db_info


@pytest.mark.usefixtures("test_setup")
class TestUpdateProduct:
    @pytest.mark.api_test
    @pytest.mark.H
    def test_update_valid_Name_product(self):
        """更新有效产品信息-产品name"""
        product_id = 1
        update_name = "lord"
        response = put_api_response(self.base_url, endpoint=f"products/{product_id}",
                                    data={"name": f"{update_name}"},
                                    token=self.token)
        # 获取api 返回
        response_json = response.json()
        # 获取db查询
        db_result = get_db_info(self.db_utils, query_sql=f"select id,name from zt_product where id='{product_id}'")
        assert response.status_code == 200, f"更新失败，状态码：{response.status_code}"
        assert response_json['id'] == db_result['id'] and response_json['name'] == db_result['name'], "更新信息与数据库查询不一致"

    def test_update_Invalid_Name_product(self):
        """更新无效产品信息-产品name"""
        product_id = 100000
        update_name = "lord"
        response = put_api_response(self.base_url, endpoint=f"products/{product_id}",
                                    data={"name": f"{update_name}"},
                                    token=self.token)
        # 获取api 返回
        response_json = response.json()
        # 获取db查询
        assert response.status_code == 400
        assert response.json()['error'] == "产品不存在"
