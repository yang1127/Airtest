# -*- encoding=utf8 -*-
import pytest
import os
from utils.tools import report_dir
from launch import launch

if __name__ == '__main__':
    # 启动连接设备模块
    launch()
    # 生成报告路径
    report_path = report_dir()
    # 运行pytest主运行程序
    pytest.main(['-s', '-q', '-k not slow', '--alluredir', report_path])
    os.system('allure generate %s -o ./report --clean' % report_path)
    os.system('allure serve %s' % report_path)
