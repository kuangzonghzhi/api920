# coding=utf-8
import time
import unittest

from public.common import mytest
from public.pages import LoginPage
from ddt import ddt, data, unpack
from loguru import logger
from public.common.datainfo import get_test_case_data, data_info
from public.common.get_img import screenshot_about_case


@ddt
class TestWorkbench(mytest.MyAutologinTest):
    """工作台模块"""

    @screenshot_about_case
    @data(*get_test_case_data(data_info, 'test_loginout'))
    def test_loginout(self, data):
        test_assert = data['assertion']
        self.workbench.close()
        loginpage = self.workbench.click_out()
        text = loginpage.get_title()
        url = loginpage.get_url()
        self.assertIn(text, test_assert['text'])
        self.assertIn(url, test_assert['url'])

    @screenshot_about_case
    def test_luandian(self):
        menus = {
            "平台管理": 1,
            "协议管理": 2,
            "机型管理": 3,
            "设备管理": 4,
            "客户管理": 5,
            "用户管理": 6,
            "权限管理": 7
        }
        for key, v in menus.items():
            self.workbench.click_menu(v)
            time.sleep(5)
