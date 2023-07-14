# -*- encoding=utf8 -*-
import allure
from airtest.core.api import *
from utils.tools import touch_image
from poco.drivers.android.uiautomation import AndroidUiautomationPoco


@allure.feature("测试小米运动模块")
class TestDemo(object):

    @classmethod
    def setup_class(cls):
        print("前置执行--步数模块开始执行:")

    @classmethod
    def teardown_class(cls):
        print("步数模块执行完毕")

    def setup_method(self):
        print("执行用例：")
        start_app("com.xiaomi.hm.health")
        self.poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
        sleep(10.0)

    def teardown_method(self):
        print("用例执行完毕")
        stop_app("com.xiaomi.hm.health")

    @allure.story('小米Life-步数1')
    def test_reg_success(self):
        print("进入步数页面:")
        self.poco(text="步数").click()
        sleep(2)

        print("执行相关用例:")
        self.poco(text="周").click()
        sleep(2)

        # 进入"月"页面，图片形式，调用重构touch方法
        touch_image(r"tpl1689316632382.png", (0.12, -0.805), (1080, 2340))
        sleep(2)

        # 退出至首页
        touch((71, 164))

        # 向下滑动，直到找到"运动记录"元素
        # 从屏幕中心向下滑动 [0.5, 0.8], [0.5, 0.2]
        while not self.poco(text="运动记录").exists():
            self.poco.swipe([0.5, 0.8], [0.5, 0.2])

        self.poco(text="查看更多").click()
        sleep(2)

        # 退出至首页
        touch((71, 164))
        sleep(2)
