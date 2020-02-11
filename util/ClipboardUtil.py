#实现剪切板功能
import pyperclip
class Clipboard:
    #模拟mac剪切板
    @staticmethod
    def getText(text):
        ##向剪切板发送文本
        pyperclip.copy(text)
        #读取剪切板文本
        text = pyperclip.paste()
        return text


if __name__ == "__main__":
    cp = Clipboard()
    print(cp.getText("test"))
