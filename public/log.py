import logging

from config import config
import json


# 测试用例输出日志
# 用例数据结构
# case_detail = {
#     'case_name':'',
#     'url': '',
#     'method': '',
#     'header': '',
#     'data': '',
#     'expect_result':'',
#     'readme': ''
# }


def case_log(case_detail, actual_result):
    """

    :param case_detail: 用例数据
    :param actual_result: 实际结果（接口的响应）
    """
    logging.info('case_name:{}'.format(case_detail.get('case_name')))
    logging.info('url:{}'.format(case_detail.get('url')))
    logging.info('expected_result:{}'.format(case_detail.get('expected_result')))
    logging.info('actual_result:{}'.format(actual_result))
    # logger.info(case_detail.get('case_name'))
    # logger.info(case_detail.get('url'))
    # logger.info(case_detail.get('expect_result'))
    # logger.info(actual_result)


# if __name__ == '__main__':
#     test_case = {
#         'case_name': 'test_case',
#         'url': 'https://www.baidu.com',
#         'method': 'post',
#         'header': '',
#         'data': {
#                 "image": "https://ai-cdn.oss-cn-shenzhen.aliyuncs.com/dev/img/6188f50e1a0083017a98af40.jpeg",
#                 "image_type": "URL",
#                 "poster_type": 1,
#                 "check_desc": "false",
#                 "clock_id": "500"},
#         'expect_result': '期望结果',
#         'readme': ''
#     }
#     case_log(test_case, "实际结果")

