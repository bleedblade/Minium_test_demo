import common.base
import json
import time

class 企业模块(common.base.BaseAction):

    def setUp(self):
        self.Authorization = common.base.BaseAction().login()
        print("这是setUp")

    def test_企业信息(self):
        headers = {
            "Authorization": self.Authorization
        }
        params = "company_id=206"
        res = common.base.BaseAction().request_api("/api/company/getItem", "GET", headers, params=params)
        assert res.find('"msg":"success"') != -1

    def test_获取行业信息(self):
        headers = {
            "Authorization": self.Authorization
        }
        res = common.base.BaseAction().request_api("/api/company/getIndustryList", "GET", headers)
        assert res.find('"msg":"success"') != -1