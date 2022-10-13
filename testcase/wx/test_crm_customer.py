import common.base
import json
import time

class 企业模块(common.base.BaseAction):

    def setUp(self):
        self.Authorization = common.base.BaseAction().login()
        print("这是setUp")

    def test_新建客户(self):
        headers = {
            "Authorization": self.Authorization
        }
        data='''{"name":"客户5","email":"","website":"","remark":"","level":"1","share_type":"1","industry":"","area":"","source":"1","address":"","life_cycle":"1","staff_id":251,"mobile":""}'''
        res = common.base.BaseAction().request_api("/api/customer/created", "POST", headers, json=json.loads(data))
        assert res.find('"msg":"success"') != -1

    def test_获取行业信息(self):
        headers = {
            "Authorization": self.Authorization
        }
        res = common.base.BaseAction().request_api("/api/company/getIndustryList", "GET", headers)
        assert res.find('"msg":"success"') != -1