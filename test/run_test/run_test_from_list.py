import sys
import os

import start_test


# test_list_name = sys.argv[1]
test_list_name = 'autoAuditTestSuite.txt'
start_test.run_from_list(test_list_name)
