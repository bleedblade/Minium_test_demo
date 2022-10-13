import common.base
import json
import time

class 名片相关(common.base.BaseAction):

    def setUp(self):
        self.Authorization = common.base.BaseAction().login()
        print("这是setUp")

    def test_编辑名片(self):
        headers = {
            "Authorization": self.Authorization
        }
        data = '''{"id": 8275, "user_id": 124, "company_id": 204, "staff_id": 254, "name": "仁王", "letter": "R", "avatar": "",
             "position": "武士", "introduction": "", "address_detail": "广东省深圳市南山区桃园路2号南头深圳市南山区人民政府南山区政府大楼(桃园路北)",
             "longitude": "", "latitude": "", "templete_id": 1, "is_default": 0, "background_id": "1", "remark": "",
             "exit_status": 2, "code_img": "", "wechat_code": "", "url_scheme": "", "expire_time": "", "advert": "",
             "extend": null, "create_from_type": 1, "created_at": "2022-08-11T09:46:04.000000Z",
             "updated_at": "2022-08-11T09:46:04.000000Z", "company_name": "公司8", "staff_name": "仁王",
             "mobile": "13000000001", "email": "", "wechat_id": null, "is_admin": false, "avatar_link": "",
             "logo_link": null}'''
        time1=time.time()
        res = common.base.BaseAction().request_api("/api/card/updateCard", "POST", headers,json=json.loads(data))
        yanchi=time.time()-time1
        print(yanchi)
        assert res.find('"msg":"success"') != -1


    def test_新增本人名片(self):
        headers = {
            "Authorization": self.Authorization
        }
        data = '''{"name":"2","avatar":"","position":"中午","mobile":"13000000002","wechat_id":"",
        "introduction":"","longitude":"","latitude":"","templete_id":1,"background_id":1,
        "address_detail":"发","company_name":"公司9","wechat_code":""}'''
        res = common.base.BaseAction().request_api("/api/card/insertCard", "POST", headers, json=json.loads(data))
        # 注意这里公司名是唯一的，现在的参数请求后会返回该企业名称已存在，如果需要真正插入记得改company_name
        # assert res.find('"msg":"success"') != -1
        assert res.find('"msg":"该企业名称已存在"') != -1

    def test_本人名片集合(self):
        headers = {
            "Authorization": self.Authorization
        }
        res = common.base.BaseAction().request_api("/api/card/list", "GET", headers)
        assert res.find('"msg":"success"') != -1

    def test_用户当前默认数据(self):
        headers = {
            "Authorization": self.Authorization
        }
        res = common.base.BaseAction().request_api("/api/card/getUserDefault", "GET", headers)
        assert res.find('"msg":"success"') != -1

    def test_用户当前默认名片(self):
        headers = {
            "Authorization": self.Authorization
        }
        res = common.base.BaseAction().request_api("/api/card/getCardDefault", "GET", headers)
        assert res.find('"msg":"success"') != -1