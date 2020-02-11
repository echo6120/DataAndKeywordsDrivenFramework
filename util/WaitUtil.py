#用于实现智能等待页面元素的出现
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WaitUtil:
    def __init__(self,driver):
        self.locationTypeDict = {
            "xpath":By.XPATH,
            "id":By.ID,
            "name":By.NAME,
            "css_selector":By.CSS_SELECTOR,
            "class_name":By.CLASS_NAME,
            "tag_name": By.TAG_NAME,
            "link_text":By.LINK_TEXT,
            "partial_link_text":By.PARTIAL_LINK_TEXT
        }
        self.driver = driver
        self.wait = WebDriverWait(self.driver,30)

    def presenceOfElementLocated(self,locatorMethod,locatorExpression,*args):
        try:
            if locatorMethod.lower().strip() in self.locationTypeDict:
                element = self.wait.until(EC.presence_of_element_located((self.locationTypeDict[locatorMethod.lower().strip()],locatorExpression)))
                return element
            else:
                raise TypeError("未找到定位方式，请确认定位方式是否正确")
        except Exception as e:
            raise e

    def frameToBeAvailableAndSwitchToIt(self,locationType,locatorExpression,*args):
        try:
            self.wait.until(EC.frame_to_be_available_and_switch_to_it((self.locationTypeDict[locationType.lower()],locatorExpression)))
        except Exception as e:
            raise e

    def visibilityOfElementLocated(self,locationType,locatorExpression,*args):
        try:
            self.wait.until(EC.visibility_of_element_located((self.locationTypeDict[locationType.lower()],locatorExpression)))
        except Exception as e:
            raise e

if __name__ == "__main__":
    # 示范
    from selenium import webdriver
    driver = webdriver.Chrome(executable_path="/Users/yu.jing/Downloads/chromedriver2")
    driver.get("https://ke.youdao.com/")
    waitutil =WaitUtil(driver)
    waitutil.presenceOfElementLocated("class_name","_3Y8-w")
    driver.quit()