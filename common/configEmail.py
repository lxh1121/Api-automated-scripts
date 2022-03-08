import os
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from Until import readConfig
import time


class send_email():
    def outlook(self, new_report):
        with open(new_report, 'r', encoding='utf8') as f:
            mail_body = f.read()
        now = time.strftime("%Y-%m-%d %H_%M_%S")
        read_conf = readConfig.ReadConfig()
        mail_server = read_conf.get_email('mail_server')
        subject = read_conf.get_email('subject') + now  # 从配置文件中读取，邮件主题
        send_addr = read_conf.get_email('send_addr')  # 从配置文件中读取，邮件发件人
        reciver_addr = read_conf.get_email('reciver_addr')  # 从配置文件中读取，邮件收件人
        username = send_addr
        password = read_conf.get_email('mail_pwd')
        message = MIMEText(mail_body, 'html', 'utf8')
        message['From'] = username
        message['to'] = reciver_addr
        message['Subject'] = Header(subject, charset='utf8')
        # qq邮箱
        # smtp = smtplib.SMTP()
        # smtp.connect(mail_server)
        # smtp.login(username, password)
        # 企业邮箱
        smtp = smtplib.SMTP_SSL(mail_server + ':465')
        smtp.login(username, password)
        smtp.sendmail(send_addr, reciver_addr.split(','), message.as_string())
        smtp.quit()



    def acquire_report_address(self, reports_address):
        # 测试报告文件夹中的所有文件加入到列表
        test_reports_list = os.listdir(reports_address)
        # 按照升序排序生成新的列表
        new_test_reports_list = sorted(test_reports_list)
        # 获取最新的测试报告
        the_last_report = new_test_reports_list[-1]
        # 最新的测试报告地址
        the_last_report_address = os.path.join(reports_address, the_last_report)
        return the_last_report_address


if __name__ == "__main__":
    new_report_addr = send_email().acquire_report_address('../result')
    send_email().outlook(new_report_addr)
    print("send email ok!!!!!!!!!")
