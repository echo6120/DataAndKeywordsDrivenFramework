#!/usr/bin/python
# coding=utf-8

import traceback
import pytest
import allure
import time
from selenium.common.exceptions import TimeoutException, NoSuchElementException

from action.PageAction import capture_screen, visit_url, assert_title
from config.Logger import init_log
from util.ObjectMap import getElement, ObjectMap
from util.WaitUtil import WaitUtil
import random
import logging

obj = ObjectMap(__file__)


class Test_login(object):
    """
    """

    @pytest.fixture(scope="class", autouse=True)
    def prepare(self,driver,env):
        with allure.step("测试数据准备:"):
            pass

        @allure.step("测试数据数据清理:")
        def fin():
            """
            Clean up test environment after testing
            """
            pass

    case,parameter = obj.getElementObject("login")
    @pytest.mark.run(order=1)
    @allure.step(title='登录')
    @pytest.mark.parametrize("case,elements_data", parameter, ids=case)
    def test_login(self,env,driver,case,api,elements_data):
        with allure.step("邮箱登录"):
            url_login = env['host']['ke'] + api['account']['login']
            visit_url(url_login)
            time.sleep(5)
            try:
                assert_title("登录-有道精品课")
                waitutil = WaitUtil(driver)
                username_obj = elements_data["userName"]
                waitutil.visibilityOfElementLocated(username_obj[0], username_obj[1])
                userName = getElement(driver,username_obj[0],username_obj[1])
                userName.send_keys(username_obj[2])

                pwd_obj = elements_data["pwd"]
                pwd = getElement(driver,pwd_obj[0],pwd_obj[1])
                pwd.send_keys(pwd_obj[2])

                login_button_obj = elements_data["loginbutton"]
                loginbutton = getElement(driver,login_button_obj[0],login_button_obj[1])

                loginbutton.click()
                time.sleep(5)
            except Exception as e:
                capturePic = capture_screen(driver)
                logging.debug("失败的截图:{}".format(capturePic))
                error_info = traceback.format_exc()
                logging.debug("error info is:{}".format(error_info))

    case, parameter = obj.getElementObject("datainfo_rename")
    @pytest.mark.run(order=2)
    @allure.step(title='账户设置更改昵称')
    @pytest.mark.parametrize("case,elements_data", parameter, ids=case)
    def test_rename(self, env,api,driver,case,elements_data):
        with allure.step("更改昵称"):
            url_rename = env['host']['ke'] + api['account']['rename']
            driver.get(url_rename)
            try:
                waitutil = WaitUtil(driver)
                nickname_obj = elements_data["nickname"]
                waitutil.visibilityOfElementLocated(nickname_obj[0], nickname_obj[1])
                nicknameelement = getElement(driver, nickname_obj[0], nickname_obj[1])
            except TimeoutException as e:
                # 捕获TimeoutException异常
                logging.debug("error info is:{}".format(traceback.print_exc()))
            except NoSuchElementException as e:
                # 捕获NoSuchElementException异常
                logging.debug("error info is:{}".format(traceback.print_exc()))
            except Exception as e:
                # 捕获其他异常
                logging.debug("error info is:{}".format(traceback.print_exc()))
            else:
                nicknameelement.clear()
                rename = u"小仙女" + str(random.randint(1, 1000))
                nicknameelement.send_keys(rename)
                # 找到页面上ID属性值为“filesubmit”的文件提交按钮对象
                submit_obj = elements_data["SubmitButton"]
                fileSubmitButton = getElement(driver, submit_obj[0], submit_obj[1])
                # 单击提交按钮，完成文件上传操作
                fileSubmitButton.click()
                time.sleep(5)

                comfirmbutton_obj = elements_data["comfirmbutton"]
                comfirmbutton = getElement(driver, comfirmbutton_obj[0], comfirmbutton_obj[1])
                comfirmbutton.click()
                time.sleep(5)
                try:
                    renickname_obj = elements_data["renickname"]
                    renickname = getElement(driver, renickname_obj[0], renickname_obj[1])
                    assert renickname.get_attribute("value") == rename,"昵称竟然没有更新成功啊"
                except Exception as e:
                    logging.debug("error info is:{}".format(e))



