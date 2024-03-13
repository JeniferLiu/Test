import pytest

from Interface_code01.candao.scripts.A_common.B_utils import post_api_response, get_db_info, delete_db_info


@pytest.mark.usefixtures("test_setup")
class TestCreateProduct:

    def check_and_delete_test_data(self, db_utils, code):
        """检查并删除已存在的测试数据"""
        query_sql = f"SELECT * FROM product_table WHERE name = '{code}'"
        existing_product = get_db_info(db_utils, query_sql)
        if existing_product:
            delete_sql = f"DELETE FROM product_table WHERE name = '{code}'"
            delete_db_info(db_utils, delete_sql)

    @pytest.mark.api_test
    @pytest.mark.H
    def test_create_right_product(self):
        """创建有效的产品信息：必填项都必填符合规范"""
        name = "jenifer"
        code = 112
        program = 10

        # 在创建新产品之前，检查并删除同名的测试数据
        self.check_and_delete_test_data(self.db_utils, code)
        # 创建
        response = post_api_response(self.base_url,
                                     endpoint=f"products",
                                     data={"name": name, "code": code, "program": program},
                                     token=self.token)
        # 创建后获取api返回
        response_json = response.json()
        # 创建后db查询
        db_result = get_db_info(self.db_utils, f"select name,code from zt_product where name='{name}'")

        # 断言
        assert response.status_code == 200, f"创建产品失败，状态码为：{response.status_code}"
        assert db_result is not None, "db查询无该产品信息"
        assert response_json['name'] == db_result['name'] and response_json['code'] == db_result[
            'code'], "产品信息与数据库查询结果不一致"

    @pytest.mark.api_test
    @pytest.mark.H
    def test_create_invalid_name_product(self):
        """创建无效的产品信息：name为空"""
        name = ""
        code = 112
        program = 10
        response = post_api_response(self.base_url,
                                     endpoint=f"products",
                                     data={"name": "", "code": code, "program": program},
                                     token=self.token)

        assert response.status_code == 400
        assert response.json()['error'] == "『产品名称』不能为空。"

    @pytest.mark.api_test
    @pytest.mark.H
    def test_create_invalid_code_product(self):
        """创建无效的产品信息：code为空"""
        name = "test1111"
        code = None
        program = 10
        response = post_api_response(self.base_url,
                                     endpoint=f"products",
                                     data={"name": f"{name}", "code": None, "program": program},
                                     token=self.token)

        assert response.status_code == 400
        assert response.json()['error'] == "『产品代号』不能为空。"

    @pytest.mark.api_test
    @pytest.mark.H
    def test_create_invalid_program_product(self):
        """创建无效的产品信息：program为空"""
        name = "test1111"
        code = 188
        program = None
        response = post_api_response(self.base_url,
                                     endpoint=f"products",
                                     data={"name": "", "code": None, "program": program},
                                     token=self.token)

        assert response.status_code == 400
        assert response.json()['error'] == "『产品』不能为空。"

# if __name__ == "__main__":
#     pytest.main(["-vs", __file__, "-m H or M",
#                  "--report=_Create_product_api_1.html",
#                  "--title=candao_接口测试报告",
#                  "--tester=jenifer",
#                  "--template=2"])
