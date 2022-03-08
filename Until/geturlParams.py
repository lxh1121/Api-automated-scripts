from Until import readConfig as readConfig

readConfig = readConfig.ReadConfig()

class geturlParams(): #定义一个方法，将从配置文件中读取的进行拼接
    def get_Url(self, type_host):
        if type_host == 'mapi':
            new_url = readConfig.get_http('scheme') + '://' + readConfig.get_http('testurl') #+ ':'+ readConfig.get_http('testport')
        else:
            new_url = readConfig.get_http('scheme') + '://' + readConfig.get_http('h5Url')
        return new_url

    def fileUploadSplit(self, url):
        file_para = url.split("/")[2]
        return file_para


geturlParams = geturlParams()


if __name__ == '__main__': #验证拼接后的正确性
    print(geturlParams().get_Url())