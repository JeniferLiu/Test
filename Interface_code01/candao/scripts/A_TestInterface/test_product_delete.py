import json

import pytest

from Interface_code01.candao.scripts.A_common.B_utils import delete_api_response, get_db_info


@pytest.mark.usefixtures("test_setup")
class TestDeleteProduct:
    @pytest.mark.api_test
    @pytest.mark.H
    def test_delete_valid_product(self):
        """删除已存在的product"""
        product_id = 3
        response = delete_api_response(self.base_url,
                                       endpoint=f"products/{product_id}",
                                       token=self.token)
        # 获取接口返回的信息
        content = json.loads(response.text)
        # db查询
        db_result = get_db_info(self.db_utils, f"select id from zt_product where id='{product_id}'")

        assert response.status_code == 200, f"删除失败，状态码为：{response.status_code}"
        assert content['message'] == "success", f"响应内容{content}"
        assert db_result is None, "产品未成功从数据库中删除"

    @pytest.mark.api_test
    @pytest.mark.H
    def test_delete_Invalid_product(self):
        """删除不存在的product"""
        product_id = 9999
        response = delete_api_response(self.base_url,
                                       endpoint=f"products/{product_id}",
                                       token=self.token)
        # 获取接口返回的信息
        content = json.loads(response.text)

        assert response.status_code == 400
        assert content['message'] == "failed", f"响应内容{content}"
