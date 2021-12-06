import unittest
import sys
from public.HTMLTestReportCN import HTMLTestRunner
from config import config
import logging
import os


def start(test_suite):
    logging.info('test start')
    with open(config.report_file, 'wb') as f:
        HTMLTestRunner(stream=f, title="TZH Api Test", description="Created by HTMLTestReportCN",
                       tester="TZH").run(test_suite)
    logging.info('test finish')


def discover():
    """

    :return: 所有测试用例（树形，有目录结构）
    """
    return unittest.defaultTestLoader.discover(config.test_case_path)


def get_all_test_cases():
    """
    去除目录结构，将所有测试用例放进一个TestSuite
    :return: 包含全部用例的TestSuite
    """
    all_cases_suite = unittest.TestSuite()

    def collect(tests):  # 递归，如果下级元素还是TestSuite则继续往下找
        if isinstance(tests, unittest.TestSuite):
            if tests.countTestCases() != 0:
                for i in tests:
                    collect(i)
        else:
            all_cases_suite.addTest(tests)  # 如果下级元素是TestCase，则添加到TestSuite中

    collect(discover())
    return all_cases_suite


def read_test_list(test_list_name):
    """
    用所选的测试用例列表的用例组装一个TestSuite
    :param test_list_name: 测试用例列表的文件名，不用带路径
    :return:
    """
    test_list_file = os.path.join(config.resource_path, test_list_name)
    # 读取txt文件中的测试用例
    with open(test_list_file) as file:
        test_list = file.readline()
    # 从所有测试用例中挑选出需要的测试用例
    all_test_cases = get_all_test_cases()
    test_suite = unittest.TestSuite()
    for case in all_test_cases:
        if case._testMethodName in test_list:
            test_suite.addTest(case)
    return test_suite


def run_from_list(test_list_name):
    start(read_test_list(test_list_name))


if __name__ == '__main__':
    run_from_list('autoAuditTestSuite.txt')
