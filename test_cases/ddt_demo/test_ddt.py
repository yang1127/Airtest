# -*- encoding=utf8 -*-
import pytest
import allure

data = [
    ("admin", "123456")
]


@allure.feature("测试DDT模块")
class TestDemo(object):
    @pytest.mark.parametrize("username, password", data)
    def test_ddt(self, username, password):
        print("用户名:%s, 密码:%s" % (username, password))
