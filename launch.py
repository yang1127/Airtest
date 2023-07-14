# -*- encoding=utf8 -*-
from airtest.core.api import *
from airtest.cli.parser import cli_setup
from utils.tools import adb_connect_emulator, get_device_id


def launch():
    # 连接模拟器
    # adb_connect_emulator()

    # 获取设备id
    device_id = get_device_id()

    # 连接
    auto_setup(__file__, logdir=True, devices=["android://127.0.0.1:5037/".format(device_id)])

    # if not cli_setup():
    #     auto_setup(__file__, logdir=True, devices=[
    #         "android://127.0.0.1:5037/{}?cap_method=MINICAP_STREAM&&ori_method=MINICAPORI&&touch_method=MINITOUCH".format(device_id)
    #     ])

    # 设置全局的超时时长为10s
    ST.FIND_TIMEOUT = 10
    ST.FIND_TIMEOUT_TMP = 10
    # 关闭截图
    ST.SAVE_IMAGE = False