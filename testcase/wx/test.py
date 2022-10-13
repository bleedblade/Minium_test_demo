import requests
import time

def request_api(self, api, method, headers, json={}, params={}, data={}):
    # host = common.readconfig.readconfig.getEnvHost(self)
    host = self.host
    if (method == "GET"):
        return requests.get(host + api, headers=headers, json=json, data=data, params=params).text
    elif (method == "POST"):
        return requests.post(host + api, headers=headers, json=json, data=data, params=params).text
    elif (method == "PUT"):
        return requests.put(host + api, headers=headers, json=json, data=data, params=params).text

time1=time.time()
header={
    "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOlwvXC9kZXYubWVpc2hpLmFyZnJvbnQuY25cL2FwaVwvbG9naW4iLCJpYXQiOjE2NjEyMzY2ODksImV4cCI6MTY2MTg0MTQ4OSwibmJmIjoxNjYxMjM2Njg5LCJqdGkiOiJCQUJGaWd6Sjg3cVZ6YlFpIiwic3ViIjoxMzksInBydiI6IjIzYmQ1Yzg5NDlmNjAwYWRiMzllNzAxYzQwMDg3MmRiN2E1OTc2ZjcifQ.tgIdryF8PyR37blGu5CDNGw6ELbOudaT57fr_cOPBhw"
}
data='''
'''
res = request_api("/api/card/updateCard", "POST", headers,json=json.loads(data))
yanchi = time.time() - time1