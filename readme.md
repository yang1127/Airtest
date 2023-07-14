# Pytest-Airtest-Allure自动化框架

## 一、项目结构

文件夹：

> images：存放图片文件
>
> log：Airtest框架所提供的日志文件
>
> report：存放生成的HTML报告
>
> reports：存放报告数据，格式为：年\_月\_日\_时\_分\_秒
>
> test_cases：重要py文件-用例集及模块用例
>
> utils：工具集


文件类：

config.py：配置属性类变量

launch.py：用于初始化连接手机和启动APP

readme.md：框架文档

requirements：第三方包---pip install -r requirements.txt

run.py：启动整体项目并输出报告

setup.cfg：pytest的配置文件，主要用于过滤不想执行的目录


## 二、项目扩展

1、DDT

~~~python
# demo
	@pytest.mark.parametrize("username,password",data)
	def test_ddt(self,username,password):
		print("用户名：%s,密码：%s"%(username,password))
~~~

2、POM

Page Object Model：一种设计模式---页面-对象-模型>>>**解耦**


## 三、面临的问题

1、自动化流程问题
2、稳定性问题
3、预留提前量不够
4、前沿技术适用度