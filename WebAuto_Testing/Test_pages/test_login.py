import pytest
from selenium import webdriver

from WebAuto_Testing.Common.utils import Utils  # 导入Utils类


class TestLogin:
    def setup_method(self):  # 每条用例执行后刷新页面
        self.bp = webdriver.Edge()

    def teardown_method(self, method):
        self.bp.refresh()

    def test_login_success(self, login):
        # 读取yml文件中的测试数据
        test_cases = Utils.read_yaml('E:/PycharmProjects/lkxtest1/WebAuto_Testing/case_data/login_testdata.yml')

        # 找到描述为登录成功测试的用例
        for test_case in test_cases:
            if test_case['描述'] == '登录成功测试':
                # 使用测试数据执行登录操作
                login.input_user(test_case['用户名'])
                login.input_pwd(test_case['密码'])
                login.click_login()
                # 断言页面是否包含特定文本
                element_text = login.get_element_text('xpath', "//h4[text()='刘欢，下午好！']")
                assert test_case['预期结果'] in element_text, f"登录成功，但页面未包含文本：{test_case['预期结果']}"
                break

    # def test_login_failure(self, login):
    #     # 读取yml文件中的测试数据
    #     test_cases = Utils.read_yaml('E:/PycharmProjects/lkxtest1/WebAuto_Testing/case_data/login_testdata.yml')
    #
    #     # 找到描述为登录失败测试的用例
    #     for test_case in test_cases:
    #         if test_case['描述'] == '登录失败测试-密码错误':
    #             # 使用测试数据执行登录操作
    #             login.input_user(test_case['用户名'])
    #             login.input_pwd(test_case['密码'])
    #             login.click_login()
    #             # 断言页面是否包含特定文本
    #             # alert = login.driver.switch_to.alert
    #             # assert test_case[
    #             #            '预期结果'] in alert.text, f"断言失败，但页面未包含文本：{test_case['预期结果']}"
    #             # break


if __name__ == '__main__':
    pytest.main(
        ["-vs",
         "E:/PycharmProjects/lkxtest1/WebAuto_Testing/Test_pages",
         "--report=_candao_v1.0",
         "--title=禅道UI自动化测试",
         "--tester=测试部分",
         "--template=2"]

    )
