import configparser
import os

class readconfig():
    def getEnvHost(self):
        conf = configparser.ConfigParser()
        conf_path = os.path.dirname(os.path.realpath(__file__)) + "\..\config\map.ini"
        conf.read(conf_path, encoding='utf8')
        isTestFlag = conf.getint("EnvHost", "isTest")
        # 获取配置文件中isTest的配置开关
        if (isTestFlag == 1):
            ENV_HOST = conf.get("EnvHost", "TestEnvHost")
            return ENV_HOST
        elif(isTestFlag == 0):
            ENV_HOST = conf.get("EnvHost", "ReleaseEnvHost")
            return ENV_HOST
        else:
            ENV_HOST = conf.get("EnvHost", "TestEnvHost")
            return ENV_HOST

