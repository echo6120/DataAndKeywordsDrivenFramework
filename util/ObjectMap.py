#用于实现定位页面元素的具体代码
from selenium.webdriver.support.ui import WebDriverWait

from util.common import get_data_path, get_test_data
from config.test import base_data

def getElement(driver,locationType,locatorExpression):
    try:
        element = WebDriverWait(driver,30).until(lambda x:x.find_element(by =locationType,value= locatorExpression))
        return element
    except Exception as e:
        raise e

def getElements(driver,locationType,locatorExpression):
    try:
        elements = WebDriverWait(driver,30).until(lambda x:x.find_elements(by =locationType,value= locatorExpression))
        return elements
    except Exception as e:
        raise e


class ObjectMap:
    def __init__(self,casepath):
        self.uiObjectMapPath =get_data_path(casepath)
        print(self.uiObjectMapPath)

    def getElementObject(self,webSiteName):
        data = get_test_data(self.uiObjectMapPath,webSiteName)
        case = []
        elements = []
        elements_data =[]
        for i in data:
            case.append(i["case"])
            elements.append(i["elements"])
            elements_data_obj = {}
            for j in i["elements"].keys():
                render_data = i["elements"][j].split(">")
                if render_data[2].startswith("$-"):
                    if render_data[2][2:] in base_data.DATA.keys():
                        render_data[2] = base_data.DATA[render_data[2][2:]]
                elements_data_obj[j] = render_data
            elements_data.append(elements_data_obj)
        list_parameters = list(zip(case, elements_data))
        return case,list_parameters


if __name__ == "__main__":
    #示范
    # from selenium import webdriver
    # driver = webdriver.Chrome(executable_path="/Users/yu.jing/Downloads/chromedriver2")
    # driver.get("https://ke.youdao.com/")
    # searchBox = getElement(driver,"xpath","//*[@id='app']/div/div[1]/div/div[2]/input")
    # searchBox.click()
    # searchBox.send_keys("曲跟")
    # alist = getElements(driver,"tag name","a")
    # print(len(alist))
    # driver.quit()
    obj = ObjectMap("/Users/yu.jing/Documents/pipenv_3/DataAndKeywordsDrivenFramework/tests/test1/test1.py")
    print(obj.getElementObject("login"))


