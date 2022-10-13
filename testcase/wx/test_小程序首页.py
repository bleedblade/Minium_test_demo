import common.base


class 小程序名片首页(common.base.BaseAction):

    def setUp(self):
        self.Authorization = common.base.BaseAction().login()
        print("这是setUp")

    def test_名片首页_默认展示名片(self):
        headers = {
            "Authorization": self.Authorization
        }
        res = common.base.BaseAction().request_api("/api/card/getCardDefault", "GET", headers)
        assert res.find('"msg":"success"') != -1

    # 不知道这个接口是干啥的
    def test_名片首页_view接口(self):
        headers = {
            "Authorization": self.Authorization
        }
        res = common.base.BaseAction().request_api("/api/views", "POST", headers)
        assert res.find('"msg":"success"') != -1