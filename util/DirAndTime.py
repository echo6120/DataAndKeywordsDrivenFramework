#获取当前日期及时间，创建异常截图存放目录
import time
from datetime import datetime
import os
#获取当前日期
from config.VarConfig import screenPicturesDir


def getCurrentDate():
    timeTup = time.localtime()
    currentDate = str(timeTup.tm_year) + "-" +str(timeTup.tm_mon) + "-" + str(timeTup.tm_mday)
    return currentDate

def getCurrentTime():
    timeStr = datetime.now()
    nowTime = timeStr.strftime('%H:%M:%S')
    return nowTime

def createCurrentDateDir():
    dirName = os.path.join(screenPicturesDir,getCurrentTime())
    if not os.path.exists(dirName):
        os.makedirs(dirName)
    return dirName

if __name__ == "__main__":
    print(getCurrentDate())
    print(getCurrentTime())
    createCurrentDateDir()