"""编写fixture:实现测试登录前置操作"""
import sys

import pytest

from WebAuto_Testing.Common.utils import Utils
from WebAuto_Testing.Pages.login_page import Login_Page


@pytest.fixture(name="login", scope="module")
def login(request):
    lp = Login_Page()
    lp.open("edge", Utils.base_url)

    login_config = Utils.read_config('login')

    lp.input_user(login_config['account'])
    lp.input_pwd(login_config['password'])
    lp.click_login()
    lp.sleep(1)
    # 获取不同测试类中调用fixture时传入的模块名称，比如：customer、batch
    module = request.param
    # 利用动态导入+反射机制实例化页面类
    __import__(f"WebAuto_Testing.Pages.{module}_page")  # 根据传入的模块名动态导入对应的页面模块
    md = sys.modules[f"WebAuto_Testing.Pages.{module}_page"]  # 将导入的模块加载到内存
    page = getattr(md, f"{module.title()}Page")  # 利用反射从导入的模块中获取到对应的页面类
    obj = page(lp.driver)  # 实例化页面类
    yield obj  # 返回页面类对象，供测试类使用
    obj.close_browser()  # 所有用例执行完成后关闭浏览器
