#coding=utf-8
import xlrd,sys
import os
import ast
from config.basic_config import ConfigInit
from config import globalparam
# from pprint import pprint
from xlutils.copy import copy
from loguru import logger


PATH = os.path.join(globalparam.data_path, ConfigInit.data_filename)  # 运行配置
# PATH = os.path.join(os.path.abspath(os.path.join(os.getcwd(), "..")), 'data\\testdata', ConfigInit.data_filename)  # 调试路径
write_path = os.path.join(globalparam.project_path,'data\\testdata', ConfigInit.data_filename)
# write_path = 'D:\\workhome\\project\\apitest\\public\\data\\testdata\\data.xlsx'

# print(PATH)
def get_excel_dict(path, index=0):
    paralList=[]
    workbook=xlrd.open_workbook(path) # 打开文件
    sheet=workbook.sheets()[index]  # sheet索引从0开始
    firstRowDataList=sheet.row_values(0)#第一行数据
    #print firstRowDataList
    for rownum in range(1, sheet.nrows):#循环每一行数据
        list = sheet.row_values(rownum)
        #print type(list[3])
        dict={}
        dictTestCaseName={}

        for caseData in list:
            dict['rownum'] = rownum
            dict[firstRowDataList[list.index(caseData)]] =caseData #每一行数据与第一行数据对应转为字典
            #json.dumps(json.loads(caseData), ensure_ascii=False)
        # print(list)
        dictTestCaseName[list[0]]=dict#转为字典后与用例名字对应转为字典
        paralList.append(dictTestCaseName)#将处理后的数据放入列表里
    return (paralList)


def get_test_case_data(data_info,testCaseName):
    testData = data_info
    getTestCaseDataList = []
    for data in testData:
        if (list(data.keys())[0]) == testCaseName:
            getTestCaseDatadict = {}
            if data[testCaseName]['send_data']:
                getTestCaseDatadict['send_data'] = ast.literal_eval(data[testCaseName]['send_data'])
            else:
                getTestCaseDatadict['send_data'] = None
            getTestCaseDatadict['assert_info'] = ast.literal_eval(data[testCaseName]['assert_info'])
            getTestCaseDatadict['method'] = data[testCaseName]['method']
            getTestCaseDatadict['url'] = data[testCaseName]['url']
            getTestCaseDatadict['case_name'] = data[testCaseName]['case_name']
            getTestCaseDatadict['rownum'] = data[testCaseName]['rownum']
            getTestCaseDataList.append(getTestCaseDatadict)

    return getTestCaseDataList

def write_res(rownum,data):
    oldwb = xlrd.open_workbook(write_path, formatting_info=True)
    newwb = copy(oldwb)
    sheet = newwb.get_sheet(0)
    sheet.write(rownum, 6, data)
    newwb.save(write_path)

data_info = get_excel_dict(PATH)
# pprint(data_info[2])
# a = get_test_case_data(data_info, 'login')
# print(a)