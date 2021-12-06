from config import config
import pandas as pd


def load_one_case(test_class_name, test_case_name):
    """
    加载一个测试用例的数据
    :param test_class_name: 测试类名
    :param test_case_name: 测试用例名
    :return: 用例数据（字典）
    {'case_name': '', 'url': '', 'method': '', 'header': ’‘, 'data': '', 'expect_result': '', 'readme': '}

    """
    work_sheet = pd.read_excel(config.case_data_file, test_class_name)  # 测试类名即是sheet名
    columns = work_sheet.columns.values  # 获取表头，列表格式
    for i in range(0, work_sheet.shape[0]):  # 忽略首行（表头）
        if work_sheet.loc[i, 'case_name'] == test_case_name:
            form_case_data = work_sheet.iloc[i, :].values  # 获取用例数据，列表格式
            break
    case_data = dict(zip(columns, form_case_data))  # 将列名和用例数据组合为字典
    return case_data


def load_cases(test_class_name):
    """
    加载整个测试类的数据
    :param test_class_name: 测试类名
    :param test_case_name: 测试用例名
    :return: 该测试类所有用例数据（列表）
    [{'case_name': '', 'url': '', 'method': '', 'header': ’‘, 'data': '', 'expect_result': '', 'readme': '},...]

    """
    work_sheet = pd.read_excel(config.case_data_file, test_class_name)  # 测试类名即是sheet名
    columns = work_sheet.columns.values  # 获取表头，列表格式
    case_data = []
    for i in range(0, work_sheet.shape[0]):  # 忽略首行（表头）
        form_case_data = work_sheet.iloc[i, :].values  # 获取用例数据，列表格式
        case_data.append(dict(zip(columns, form_case_data)))  # 将列名和用例数据组合为字典
    return case_data


if __name__ == '__main__':
    test_data = load_cases('TestAutoAudit')
    print(test_data)



