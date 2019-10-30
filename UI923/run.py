# coding=utf-8

import unittest
import HTMLTestRunner
import time
import os
from loguru import logger
from config import globalparam
from public.common import sendmail
from testcase import test_login, test_workbench

path = os.path.join(os.path.abspath('.'), 'report', 'log', 'test_{}.log'.format(time.strftime('%Y-%m-%d')))
logger.add(path)  # 日志初始化


def run(method, test=None):
	if method == 'all':
		test_dir = "./testcase"
		suite = unittest.defaultTestLoader.discover(start_dir=test_dir, pattern='*.py')
		
		now = time.strftime('%Y-%m-%d_%H_%M_%S')
		reportname = globalparam.report_path + '\\' + 'TestResult' + now + '.html'
		with open(reportname, 'wb') as f:
			runner = HTMLTestRunner.HTMLTestRunner(
				stream=f,
				title='测试报告',
				description='Test the import testcase'
			)
			runner.run(suite)
		time.sleep(3)
		# 发送邮件
		mail = sendmail.SendMail()
		# mail.send()
	if method == 'one':
		suit = unittest.TestSuite()
		suit.addTest(test)  # 把这个类中需要执行的测试用例加进去，有多条再加即可
		runner = unittest.TextTestRunner()
		runner.run(suit)


if __name__ == '__main__':
	#  run('one', test_workbench.TestWorkbench("test_luandian"))
	run('all')
