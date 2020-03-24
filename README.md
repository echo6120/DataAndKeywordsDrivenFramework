利用pytest自身的优点，在conftest.py中增加fixture和hook函数

1.hook函数

pytest_addoption：增加自定义参数输入：env，从而判断测试环境读取对应的测试数据

pytest_collection_modifyitems：测试用例收集完成时，将收集到的item的name和nodeid的中文显示在控制台上

2.fixture：

driver():在测试开始前，声明webdriver，测试结束后自动关闭浏览器

log()：在测试开始前，初始化log

api():在测试开始前，返回url

env()：返回对应环境下的测试数据

各个文件的大致介绍：

--config包：用于实现框架中的各种配置信息
	
	--Logger.py日志的配置文件 
	--setting.py:存储url的信息 
	--VarConfig:常用地址chromeDriverFilePath，parentDirPath等
	--按照测试环境创建test文件夹，下面存储test环境的测试数据，base_data 存储测试数据，test_config存储host等信息 

--util包：实现测试过程中调用的工具类方法，

	-- ObjectMap.py用于实现定位页面元素的具体代码,例如getElement,getElements方法 
	--将data文件夹下，获取页面的定位元素和定位表达式进行处理，处理后返回case,list_parameters ，在具体case中利用pytest的			   pytest.mark.parametrize装饰器，引入测试data
	-- ClipboardUtil.py剪切板操作封装
	-- common.py get_data_path,get_test_data封装
	-- 日期等常用函数封装
	-- waitutil.py 用于实现智能等待页面元素的出现  

--data目录 存放测试数据

--tests目录  存放测试脚本

--action目录 实现具体页面的动作的封装,比如输入数据，点击按钮,异常错误截图等
