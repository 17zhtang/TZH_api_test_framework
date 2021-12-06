import logging

import requests
import unittest
import json
from config import config
from public import form
from public import log


# 测试用例基类
class BasicCase(unittest.TestCase):  # 继承TestCase
    @classmethod
    def setUpClass(cls):
        if cls.__name__ != 'BasicCase':
            cls.case_data_array = form.load_cases(cls.__name__)  # 加载测试类所有用例数据,放在类下，方便其他方法调用

    def get_expected_result(self,case_name):
        case_data = self.get_case_data(case_name)
        expected_result = case_data.get('expected_result')
        return expected_result

    # 从case_data_array中拿到指定用例的数据
    def get_case_data(self, case_name):
        flag = False
        for i in range(0, len(self.case_data_array)):
            if self.case_data_array[i].get('case_name') == case_name:
                flag = True
                case_data = self.case_data_array[i]
        if flag:
            return case_data
        else:
            logging.info('找不到用例:'+case_name)
            return None

    def send_requests(self, case_name):
        """
        如果后期需要更多的请求参数，修改该方法和case.xlsx的表头
        :param case_name: 用例名称
        :return: 响应
        """
        case_data = self.get_case_data(case_name)
        url = case_data.get('url')
        method = case_data.get('method').upper()
        header = case_data.get('header')
        data = case_data.get('data')
        expected_result = case_data.get('expected_result')
        readme = case_data.get('readme')
        if method == 'POST':
            # json.loads字符串转json， 表格中的数据为空时，pandas读到的为nan，json.loads(nan)会报格式错误
            # 是headers不是header
            actual_result = requests.post(url=url, json=json.loads(data), headers=json.loads(header))
        elif method == 'GET':
            actual_result = requests.get(url=url, params=json.loads(data), headers=json.loads(header))
        log.case_log(case_data, actual_result.text)
        return actual_result.text  # 直接返回actual_result的话是响应码，actual.result.text是响应体

