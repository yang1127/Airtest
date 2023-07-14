# -*- encoding=utf8 -*-
import re
import sys
from faker import Faker
from airtest.core.api import *
from config import emulator_dict


# 生成报告数据目录路径
def report_dir():
    report_path = './reports/data/' + time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime(time.time()))
    return report_path


# 重构touch函数
def touch_image(i_name, record_pos, resolution):
    images_path = r'./images/'
    template_path = images_path + i_name
    template = Template(template_path, record_pos=record_pos, resolution=resolution)
    return touch(template)


# adb连接模拟器函数
def adb_connect_emulator():
    for i, v in emulator_dict.items():
        print("正在连接模拟器：{}".format(i), v)
        os.system(v)
        sleep(1)


# 获取已连接设备id，并输出
def get_device_id():
    str_init = ""
    all_info = os.popen("adb devices").readlines()
    print("adb devices 输出的内容是:", all_info)

    for i in range(len(all_info)):
        str_init += all_info[i]
    devices_name = re.findall('\n(.+?)\t', str_init, re.S)
    # print('所有设备名称：\n', devices_name)
    try:
        return devices_name[0]
    except IndexError:
        print("没有找到已连接的设备")
        sys.exit()
    except:
        print("未知异常")


# 生成测试数据 - Faker第三方包
def faker_data(num):
    faker = Faker('zh_CN')
    list_data = []
    for i in range(num):
        list_data.append((faker.name(), faker.ssn(), faker.phone_number()))
    return list_data

