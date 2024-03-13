import pytest

from Interface_code01.candao.scripts.A_common.B_utils import get_db_info, get_api_response


@pytest.mark.usefixtures("test_setup")
class TestProductList:

    def get_db_total_products(self):
        query_sql = "select count(*) as total from zt_product"
        result = get_db_info(self.db_utils, query_sql)
        return result['total'] if result else None

    @pytest.mark.api_test
    @pytest.mark.H
    def test_get_product_list_with_token(self):
        response = get_api_response(self.base_url, "products", self.token)
        assert response.status_code == 200, "请求失败，状态码：{}".format(response.status_code)

        productslist = response.json()
        db_total = self.get_db_total_products()
        assert productslist['total'] == db_total, "接口返回的产品总数与数据库不一致"

    @pytest.mark.api_test
    @pytest.mark.H
    def test_get_product_list_without_token(self):
        response = get_api_response(self.base_url, "products")
        assert response.status_code in [401, 403], "未授权或禁止访问，实际状态码：{}".format(response.status_code)

# if __name__ == "__main__":
#     pytest.main(["-vs", __file__, "-m H or M",
#                  "--report=_getproductList_api_1.html",
#                  "--title=candao_接口测试报告",
#                  "--tester=jenifer",
#                  "--template=2"])
