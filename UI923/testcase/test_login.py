import time
import unittest

from public.common import mytest
from public.pages import LoginPage
from ddt import ddt,data,unpack
from loguru import logger
from public.common.datainfo import get_test_case_data, data_info
from public.common.get_img import screenshot_about_case


@ddt
class TestLogin(mytest.MyTest):
    """登录模块"""

    @screenshot_about_case
    @data(*get_test_case_data(data_info, 'test_01_login'))
    def test_01_login(self, data):
        """正常登录"""
        test_data = data['data']
        test_assert = data['assertion']
        login = LoginPage.Login(self.dr)
        ele = login.login(test_data['username'],test_data['pw'])
        username = ele.get_name()
        url = ele.get_url()
        self.assertIn(url,test_assert['title'])
        self.assertIn(username, test_assert['username'])

