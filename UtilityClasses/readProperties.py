import configparser

rawConfigParserObj=configparser.RawConfigParser()
rawConfigParserObj.read(".\\Configuration\\config.ini")



class ReadConfig:

    @staticmethod
    def getAppCred(group,key):
        data=rawConfigParserObj.get(group,key)
        return data


