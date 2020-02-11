#定义整个框架中所需要的全局常量值
import os

chromeDriverFilePath = "/Users/yu.jing/Downloads/chromedriver2"

#获取当前文件夹所在目录的父目录的绝对路径
parentDirPath = os.path.dirname(os.path.abspath(__file__))
#异常照片存放目录
screenPicturesDir = parentDirPath + "/exceptionpictures"

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if __name__ == "__main__":
    print(BASE_DIR)