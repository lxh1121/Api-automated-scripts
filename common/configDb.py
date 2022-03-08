#coding=utf-8
import pymysql.cursors
from Until import readConfig
import json
import os
import datetime

read_config = readConfig.ReadConfig()
class OperationMysql(object):
    def __init__(self):
        """
        数据库操作
        :return:
        """
        self.conn = pymysql.connect(
            host=read_config.get_mysql('testhost'),
            user=read_config.get_mysql('testuser'),
            passwd=read_config.get_mysql('testpasswd'),
            port=int(read_config.get_mysql('port')),
            db=read_config.get_mysql('db'),
            charset=read_config.get_mysql('charset'),
            # cursorclass=pymysql.cursors.DictCursor  #使返回值是dict
        )
        self.cur = self.conn.cursor()


    def sql_select(self, sql, fieldValue):
        self.cur.execute(sql, fieldValue)
        data = self.cur.fetchall()
        self.cur.close()
        self.conn.close()
        return data


    def db_backup(self):
        """数据库备份"""
        if not os.path.exists('mysqldb_backup'):
            os.mkdir('mysqldb_backup')
        os.chdir('mysqldb_backup')

        today = datetime.date.today()
        yesterday = today - datetime.timedelta(days=5)

        today_file_name = "/home/******/mysqldb_backup/mysql" + str(today) + ".sql"
        yesterday_file_name = "/home/******/mysqldb_backup/mysql" + str(yesterday) + ".sql"

        response_code = os.system(
            "/usr/local/mysql/bin/mysqldump -u 数据库用户名 -p数据库密码 -h 数据库IP 数据库名称 > /home/******/mysqldb_backup/mysql`date +%Y-%m-%d`.sql")

        file_size = int(os.path.getsize(today_file_name)) / 1024

        if response_code == 0:
            text = "#### Message:\n\n > - MySqlDB Backup Completed!\n\n > - SQL_file_size:" + str(
                round(file_size, 4)) + "KB"
            if os.path.exists(yesterday_file_name):
                os.remove(yesterday_file_name)
        else:
            text = "#### Message:\n\n > - MySqlDB Backup Error!\n\n > - Please check the server program."

        # dingding_url = "https://oapi.dingtalk.com/robot/send?access_token=钉钉机器人接口token"
        # headers = {"Content-Type": "application/json; charset=utf-8"}
        #
        # post_data = {
        #     "msgtype": "markdown",
        #     "markdown": {
        #         "title": "MySqlDB Backup Message",
        #         "text": text
        #     }
        # }
        #
        # requests.post(dingding_url, headers=headers, data=json.dumps(post_data))


    def db_restore(self):
        """数据库还原"""
        pass



import random
if __name__ == "__main__":
    sql_three = 'SELECT id FROM city_area WHERE pid in (SELECT id FROM city_area WHERE pid in (SELECT id FROM city_area WHERE pid = %s))'
    sql_two = "SELECT id FROM city_area WHERE pid in (SELECT id FROM city_area WHERE pid = %s)"
    mysql = OperationMysql()
    value = ['0']
    data = mysql.sql_select(sql_two, value)
    print(data)
    print(data[0].get('id'))
    print(random.choice(data).get('id'))
    # for i in data:
    #     print(i.get('id'))
    # for i in data:
    #     print(type(i[0]))
    # data = {'areaId': '213', "zcx": "da"}
    # print(data.get("areaId"))
    # data["areaId"] = '123'
    # print(data)
    # data_one = ['userAddress_02', '新增地址', 'yes', '', '', '/mall/address/add', 'post',
    #             '{"areaId":"", "areaName":"北京北京市东城区", "detailAddress":"长宁庄园283从v7弄右侧大庄园", "receiveName":"路", "state":"2", "tel":"18737553592"}','', 'yes', 'errorcode', '{"code": 1}', 'yes', '通过', '']
    # da1 = json.loads(data_one[7])
    # da1["areaId"] = '111'
    # print("%s通过"%da1)