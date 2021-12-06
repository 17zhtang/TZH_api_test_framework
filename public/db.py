# 封装数据库操作
import pymysql
from config import config


class DateBase:

    # 初始化对象
    def __init__(self):
        db = config.pjx
        self.connect = pymysql.connect(host=db.get("host"),
                                       port=db.get("port"),
                                       user=db.get("user"),
                                       passwd=db.get("passwd"),
                                       db=db.get("db"),
                                       charset=db.get("charset"))

        self.cursor = self.connect.cursor()

    # 销毁对象
    def __del__(self):
        self.cursor.close()
        self.connect.close()

    # 查询语句
    def query(self, sql):
        self.cursor.execute(sql)
        print("sql执行成功query")
        return self.cursor.fetchall()

    # 执行语句
    def execute(self, sql):
        try:
            self.cursor.execute(sql)
            self.connect.commit()
        except Exception as e:
            self.connect.rollback()
            print("sql执行出错", str(e))
        else:
            print("sql执行成功execute")


# 测试
# if __name__ == '__main__':
#     test_db = DateBase()
#     sql = "select * from pjx.course where code='K3S1101'"
#     result = test_db.query(sql)
#     print(result)
