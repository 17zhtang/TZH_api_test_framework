# 将根目录加入sys.path中,解决命令行找不到包的问题
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(os.path.split(curPath)[0])[0]
sys.path.append(rootPath)

# if __name__ == '__main__':
#     print(curPath)
#     print(rootPath)
