# -*-coding:utf-8 -*-
import os
import unittest
from datetime import datetime
from functools import wraps
from config.basic_config import ConfigInit
from config import globalparam
from loguru import logger

"""
此模块用于屏幕截图
"""
# 获取截截图保存的路径
img_base_path = os.path.join(globalparam.img_path)

# case 断言失败截图装饰器
def screenshot_about_case(func):
    # 保持传入的case的名称不被装饰器所改变
    @wraps(func)
    # t = func
    def get_screenshot_about_case(self, *args, **kwargs):
        try:
            func(self, *args, **kwargs)
        except Exception as e:
            # 获取case_name的名称
            case_name = '{}'.format(unittest.TestCase.id(self))
            # 截屏的路径
            screenshotPath = os.path.join(img_base_path, case_name)
            # 获得现在的时间戳
            time_now = datetime.now().strftime('%Y%m%d%H%M%S')
            # 名字的一部分
            screen_shot_name = "NG.png"
            # 组装图片需要传入的路径和推片名称
            screen_img = screenshotPath + '_' + time_now + '_' + screen_shot_name
            # 截图并保存到相应的名称的路径
            self.dr.take_screenshot(screen_img)
            raise e
    return get_screenshot_about_case
