import os
import logging

# 路径设置
project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 项目路径
test_case_path = os.path.join(os.path.join(project_path, 'test'), 'test_case')  # 测试用例路径
resource_path = os.path.join(project_path, "resource")  # 资源路径
logs_path = os.path.join(project_path, "logs")  # 日志目录
reports_path = os.path.join(project_path, "reports")  # 报告路径
case_data_file = os.path.join(resource_path, "case.xlsx")  # 用例数据文件
log_file = os.path.join(logs_path, "test.log")  # 日志文件
report_file = os.path.join(reports_path, "report.html")  # 报告文件

# 数据库配置
pjx = {"host": "172.16.253.113",
       "port": 3306,
       "user": "root",
       "passwd": "dbtest",
       "db": "pjx",
       "charset": "utf8"
       }

# log基础设置
# 需要把logging初始化的FileHandler的encode改为'utf-8'解决日志中文乱码
logging.basicConfig(level=logging.DEBUG,
                    filemode="a",  # 追加模式
                    filename=log_file,
                    format="%(levelname)s %(asctime)s %(filename)s %(lineno)d %(funcName)s %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S"
                    )
# file_handler = logging.FileHandler(filename='test.log', encoding='utf-8', mode='a')  # 解决日志中文乱码
# formater = logging.Formatter("%(levelname)s %(asctime)s %(filename)s %(lineno)d %(funcName)s %(message)s")
# file_handler.setFormatter(fmt=formater)
# logger = logging.getLogger()
# logger.addHandler(file_handler)

