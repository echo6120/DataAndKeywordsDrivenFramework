
from selenium import webdriver
import pytest

from action.PageAction import open_browser, maximize_browser
from config.Logger import init_log
from config.VarConfig import chromeDriverFilePath, BASE_DIR
import yaml
from config.test import base_data
from config.settings import APIS



@pytest.fixture(scope="session",autouse=True)
def driver():
    """
    声明webdriver
    """
    driver = open_browser("chrome")
    maximize_browser()
    yield driver
    # 执行完再关闭
    driver.quit()

@pytest.fixture(scope="session",autouse=True)
def log():
    """
    初始化log
    """
    init_log()

def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的item的name和nodeid的中文显示在控制台上
所有的测试用例收集完毕后调用, 可以再次过滤或者对它们重新排序
 items （收集的测试项目列表）
    """
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")

def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="test", help="environment: dev or test or integration")


@pytest.fixture(scope="session", autouse=True)
def api():
    return APIS

@pytest.fixture(scope="session", autouse=True)
def env(request):
    """
    Parse env config info
    :param request:
    :param cmdopt:
    :return:
    """
    environ = request.config.getoption("--env")
    config_path = '{0}/config/{1}/{1}_config.yml'.format(BASE_DIR, environ)
    with open(config_path) as f:
        env_config = yaml.load(f)
    env_config['config_path'] = config_path
    base  =  base_data.DATA
    env_config['base_data'] = base
    return env_config


