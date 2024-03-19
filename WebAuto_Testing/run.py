import pytest

from WebAuto_Testing.Common.utils import Utils

if __name__ == '__main__':
    pytest.main(
        ["-vs",
         Utils.test_path,
         "--report=_candao_v1.0",
         "--title=禅道UI自动化测试",
         "--tester=测试部分",
         "--template=2"]

    )
