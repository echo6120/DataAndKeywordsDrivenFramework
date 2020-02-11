#实现具体页面的动作的封装
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from config.VarConfig import chromeDriverFilePath
from util.DirAndTime import getCurrentTime, createCurrentDateDir
from util.ObjectMap import getElement
from util.WaitUtil import WaitUtil

driver = None
waitUtil = None

def open_browser(browserName,*args):
    global driver,waitUtil
    try:
        if browserName.lower() == "chrome":
            chrome_options = Options()
            chrome_options.add_experimental_option("excludeSwitches",["ignore-certificate-errors"])
            driver = webdriver.Chrome(executable_path= chromeDriverFilePath,chrome_options = chrome_options)

        else:
            print("你用的不是Chrome浏览器，暂时不支持别的浏览器")
        waitUtil = WaitUtil(driver)
        return driver
    except Exception as e:
        raise e

def visit_url(url,*args):
    global driver
    try:
        driver.get(url)
    except Exception as e:
        raise e

def close_browser(*args):
    global driver
    try:
        driver.quit()
    except Exception as e:
        raise e

def sleep(sleepSeconds,*args):
    try:
        time.sleep(int(sleepSeconds))
    except Exception as e:
        raise e

def clear(locationType,locatorExpression,*args):
    global driver
    try:
        getElement(driver,locationType,locatorExpression).clear()
    except Exception as e:
        raise e

def input_string(locationType,locatorExpression,inputContent):
    global driver
    try:
        getElement(driver, locationType, locatorExpression).send_keys(inputContent)
    except Exception as e:
        raise e

def click(locationType,locatorExpression):
    global driver
    try:
        getElement(driver, locationType, locatorExpression).click()
    except Exception as e:
        raise e

def assert_string_in_pagesource(assertString,*args):
    global driver
    try:
        assert assertString in driver.page_source,u"%s not found in bage source" %assertString
    except AssertionError as e:
        raise AssertionError(e)
    except Exception as e:
        raise e

def assert_title(titleStr,*args):
    global driver
    try:
        assert titleStr in driver.title,u"%s not found in title" %titleStr
    except Exception as e:
        raise e

def getTitle(*args):
    global driver
    try:
        return driver.title
    except Exception as e:
        raise e

def getPageSource(*args):
    global driver
    try:
        return driver.page_source
    except Exception as e:
        raise e

def switch_to_frame(locationType, frameLocatorExpression, *arg):
    # 切换进入frame
    global driver
    try:
        driver.switch_to.frame(getElement
            (driver, locationType, frameLocatorExpression))
    except Exception as err:
        raise err

def switch_to_default_content(*arg):
    # 切出frame
    global driver
    try:
        driver.switch_to.default_content()
    except Exception as err:
        raise err

def maximize_browser():
    # 窗口最大化
    global driver
    try:
        driver.maximize_window()
    except Exception as err:
        raise err

def capture_screen(*args):
    # 截取屏幕图片
    global driver
    currTime = getCurrentTime()
    picNameAndPath = str(createCurrentDateDir()) + "/" + str(currTime) + ".png"
    try:
        driver.get_screenshot_as_file(picNameAndPath)
    except Exception as err:
        raise err
    else:
        return picNameAndPath

def waitPresenceOfElementLocated(locationType, locatorExpression, *arg):
    '''显示等待页面元素出现在DOM中，但并一定可以见，
            存在则返回该页面元素对象'''
    global waitUtil
    try:
        element = waitUtil.presenceOfElementLocated(locationType, locatorExpression)
        return element
    except Exception as err:
        raise err

def waitFrameToBeAvailableAndSwitchToIt(locationType, locatorExpression, *args):
    '''检查frame是否存在，存在则切换进frame控件中'''
    global waitUtil
    try:
        waitUtil.frameToBeAvailableAndSwitchToIt(locationType, locatorExpression)
    except Exception as err:
        raise err

def waitVisibilityOfElementLocated(locationType, locatorExpression, *args):
    '''显示等待页面元素出现在DOM中，并且可见，存在返回该页面元素对象'''
    global waitUtil
    try:
        element = waitUtil.visibilityOfElementLocated(locationType, locatorExpression)
        return element
    except Exception as err:
        raise err

if __name__ == "__main__":
    from selenium import webdriver
    driver = webdriver.Chrome(executable_path="/Users/yu.jing/Downloads/chromedriver2")
    driver.get("https://ke.youdao.com/")
    #maximize_browser()
    capture_screen()
