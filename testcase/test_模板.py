import common.base


class Test(common.base.BaseAction):

    def setUp(self):
        self.Authorization = common.base.BaseAction().login()
        print("这是setUp")

    def test_名片首页_默认展示名片(self):  # 哇真的能用中文命名文件和函数哎！
        headers = {
            "Authorization": self.Authorization
        }
        res = common.base.BaseAction().request_api("/api/card/itemMeDefault", "GET", headers)
        assert res.find('"message":"success"') != -1

