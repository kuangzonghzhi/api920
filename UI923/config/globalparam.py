#coding=utf-8

import os
import time
# from public.common.readconfig import ReadConfig

# 读取配置文件
# config_file_path = os.path.split(os.path.realpath(__file__))[0]
# read_config = ReadConfig(os.path.join(config_file_path,'config.ini'))
# 项目参数设置
# prj_path = read_config.getValue('projectConfig','project_path')

#项目路径
project_path = os.path.abspath('.')
# 日志路径
log_path = os.path.join(project_path, 'report', 'log', 'test_{}.log'.format(time.strftime('%Y-%m-%d')))
# 截图文件路径
img_path = os.path.join(project_path, 'img')
# 测试报告路径
report_path = os.path.join(project_path, 'report', 'html_report')
# 默认浏览器
browser = 'Chrome'
# 是否开启静默模式,只有在chrome下支持开启
headless = False

# 测试数据路径
data_path = os.path.join(project_path, 'data', 'testdata')

