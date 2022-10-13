import requests
import minium
import json
import common.readconfig


class BaseAction(minium.MiniTest):
    # 微信小程序初始化，启动本机微信开发者工具，记得需提前登录
    # 这两个具体路径可参考：https://minitest.weixin.qq.com/#/minium/Python/introduction/quick_start?id=%e5%bf%85%e8%a6%81%e7%9a%84%e7%9f%a5%e8%af%86
    mini = minium.Minium({
        "project_path": "C:\\Users\\admin\\Documents\\meishi_uniapp_devlop_new\\meishi_mini_uniapp\\unpackage\\dist\\dev\\mp-weixin",
        # 替换成你的【小程序项目目录地址】
        "dev_tool_path": "D:\Program Files (x86)\Tencent\微信web开发者工具\cli.bat"
        # 替换成你的【开发者工具cli地址】，macOS: <安装路径>/Contents/MacOS/cli， Windows: <安装路径>/cli.bat
    })

    # 读map.ini文件获取当前设置的环境域名
    host = common.readconfig.readconfig().getEnvHost()
    print("host" + host)

    # 将json字符串转换成字典的工具方法
    def json_to_dict(self, data):
        dict_data = json.loads(data)
        return dict_data

    # 获取微信小程序登录码
    def getWXMethodLoginCode(self):
        # 通过登录了微信号的开发者工具调用微信小程序登录方法，获取当前该微信号有效的code，用于后续登录。
        # 小程序登录流程：https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/login.html
        promise = self.mini.call_wx_method("login")
        return promise["result"]["result"]["code"]

    # 携带微信小程序登录有效code请求项目服务器获取有效user_token
    def login(self):
        # 调用一下上面那个获取微信小程序登录码的函数
        logincode = BaseAction().getWXMethodLoginCode()
        loginpostdata = {
            "code": logincode
        }

        # 携带获得的微信code请求服务器登录接口
        res = requests.post(self.host + "/api/login", data=loginpostdata)
        responsedata = BaseAction().json_to_dict(res.text)
        # 获取有效token
        Authorization = str(responsedata["data"]["token_type"] + " " + responsedata["data"]["access_token"])
        return Authorization

    # 请求的封装，还需要啥自己加，返回响应体
    def request_api(self, api, method, headers, json={}, params={}, data={}):
        # host = common.readconfig.readconfig.getEnvHost(self)
        host = self.host
        if (method == "GET"):
            return requests.get(host + api, headers=headers, json=json, data=data, params=params).text
        elif (method == "POST"):
            return requests.post(host + api, headers=headers, json=json, data=data, params=params).text
        elif (method == "PUT"):
            return requests.put(host + api, headers=headers, json=json, data=data, params=params).text
