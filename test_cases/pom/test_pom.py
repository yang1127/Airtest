# -*- encoding=utf8 -*-
import allure
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco


class PageBase(object):
    def __init__(self):
        pass


@allure.feature("测试网易云音乐模块")
class TestCases(object):

    @classmethod
    def setup_class(cls):
        print("前置执行 -- 网易云音乐模块开始执行:")

    @classmethod
    def teardown_class(cls):
        print("网易云音乐模块执行完毕")

    def setup_method(self):
        print("执行用例：")
        start_app("com.netease.cloudmusic")
        self.poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
        sleep(0.5)

    def teardown_method(self):
        print("用例执行完毕")
        stop_app("com.netease.cloudmusic")

