import datetime
import os
import json

def get_data_path(case_path):
    """
    :param case_path:
    :return:
    """

    file_name = os.path.dirname(case_path).split(os.sep + 'tests' + os.sep, 1)
    test_data = os.sep.join([file_name[0], 'data', file_name[1], os.path.basename(case_path).replace('.py', '.json')])
    if os.path.isfile(test_data):
        return test_data
    else:
        test_data = os.sep.join(
            [file_name[0], 'data', file_name[1],
             os.path.basename(case_path).replace('.py', '.json').replace('test_', '')])
        return test_data


def get_test_data(test_data_path,WebsiteName):
    """
    Get test data from json
    :param test_data_path:
    :return: case name, precondition data , and test data
    """
    with open(test_data_path) as f:
        dat = json.loads(f.read())
        tests = dat['tests']
        tests_data = tests[WebsiteName]
        return tests_data


if __name__ == "__main__":
    #print(get_data_path("/Users/yu.jing/Documents/pipenv_3/DataAndKeywordsDrivenFramework/tests/test1/test1.py"))
    #print(get_test_data("/Users/yu.jing/Documents/pipenv_3/DataAndKeywordsDrivenFramework/data/test1/test1.json","login"))
    pass