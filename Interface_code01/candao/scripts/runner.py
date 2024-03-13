# 运行用例控制器
import pytest

pytest.main(["A_TestInterface", "-v", "-s", "--report=_getproductList_api_1.html",
             "--title=candao_接口测试报告",
             "--tester=jenifer",
             "--template=2"])  # 指定case目录运行
