# 小程序接口自动化项目

## 安装环境：

Windows 10

Python3.10（理论上3就行）

微信开发者工具（需登录微信号）

微信小程序项目代码

Python IDE（推荐PyCharm）

本项目因为涉及小程序相关接口的调用，所以需要使用 minium 框架，官方文档：https://minitest.weixin.qq.com/#/minium/Python/readme ， 安装库：

```
pip3 install https://minitest.weixin.qq.com/minium/Python/dist/minium-latest.zip
```

## 项目文件目录：

```
common  文件夹存放公用方法
	base.py  小程序初始化、登录、接口请求方法封装等
	readconfig.py  用于读取config/map.ini中的配置
config  存放配置文件
	map.ini  配置文件，目前仅有切换环境域名的配置
testcase  用于存放测试用例
	wx  用于存放微信小程序接口用例
		test_001.py  具体接口用例可执行文件
suite.json  项目测试计划配置文件
outputs  运行项目后minium会自动生成outputs文件夹存放测试报告
```

运行前记得替换common/base.py文件下的配置路径，具体路径可参考：[Minitest-环境检查-必要的知识](https://minitest.weixin.qq.com/#/minium/Python/introduction/quick_start?id=%e5%bf%85%e8%a6%81%e7%9a%84%e7%9f%a5%e8%af%86)

```
mini = minium.Minium({
    "project_path": "C:\\Users\\admin\\Documents\\meishi_mini_uniapp\\meishi_mini_uniapp\\unpackage\\dist\\dev\\mp-weixin",
    # 替换成你本机的【小程序项目目录地址】
    "dev_tool_path": "D:\Program Files (x86)\Tencent\微信web开发者工具\cli.bat"
    # 替换成你本机的【开发者工具cli地址】，macOS: <安装路径>/Contents/MacOS/cli， Windows: <安装路径>/cli.bat
})
```

## 运行项目

开始前需要先打开9420端口

```
"path/to/cli" auto --project "path/to/project" --auto-port 9420
```

如果端口被占用就cmd看一下手动删一下进程

```
netstat -ano | findstr "9420"
```

### 单用例运行

点击项目用例函数前的执行按钮执行单个用例。如果没有执行按钮需检查用例类继承情况。

### 整体运行

项目根目录下命令行输入：

```
minitest -s suite.json -g
```

-g 是生成测试报告

suite.json文件用于匹配需要执行的用例，具体可见官方文档 [MiniTest-测试计划](https://minitest.weixin.qq.com/#/minium/Python/framework/suite)

## 查看测试报告

在终端命令行，项目根目录下执行如下命令。执行后若无事发生可将python3改为python重新执行。此处outputs即为上文整体运行项目后在项目根目录下自动生成的测试结果文件夹，包含执行过的结果记录。

```
python3 -m http.server 12345 -d outputs
```

服务成功启动后浏览器访问 localhost:12345 查看测试报告