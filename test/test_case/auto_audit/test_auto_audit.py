import unittest

from test.test_case import basic_case


class TestAutoAudit(basic_case.BasicCase):  # 继承BasicCase，间接继承unittest.TestCase
    #  已有self.case_data_array
    def test_auto_audit_gubi_success(self):
        """
        咕比机器审核
        """
        expected_result = self.get_expected_result('test_auto_audit_gubi_success')
        actual_result = self.send_requests('test_auto_audit_gubi_success')
        self.assertIn(expected_result, actual_result)
        print(actual_result)


# if __name__ == '__main__':
#     test_case = TestAutoAudit()
#     test_result = test_case.send_requests()
#     print(test_result)

if __name__ == '__main__':  # 如果是直接从当前模块执行（非别的模块调用本模块）
    unittest.main(verbosity=2)
