#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header


def send_email(info):
    # 使用第三方 SMTP 服务（请自行修改）
    # 以QQ为例
    mail_host = "smtp.qq.com"  # 设置服务器
    mail_user = "1934109821@qq.com"  # 用户名（你的QQ账号@qq.com）
    mail_pass = "vpnvpmnmzadgcfef"  # 口令（先要开启SMTP，口令是16位字母）

    # 发件人邮箱
    sender = '1934109821@qq.com'
    # 收件人邮箱
    receivers = ['1934109821@qq.com']

    # 邮件内容
    message = MIMEText(info, 'plain', 'utf-8')
    message['From'] = Header("腾讯云打卡", 'utf-8')
    message['To'] = Header("自己", 'utf-8')
    # 邮件主题
    subject = info
    message['Subject'] = Header(subject, 'utf-8')

    try:
        # 连接smtp服务器
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
        smtpObj.login(mail_user, mail_pass)
        # 发送邮件
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("无法发送邮件")
