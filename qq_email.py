"""
qq邮箱用程序发邮件
"""
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr


def send_email():
    # 邮箱配置
    # 邮件文本内容
    msg = MIMEText('{}'.format(content), 'html', 'utf-8')
    # 邮件上显示的发件人
    msg['From'] = formataddr(['{}'.format(addressor), '{}@qq.com'.format(letter_writer)])
    # 邮件上显示的主题
    msg['Subject'] = "{}".format(motif)

    # 发邮件
    server = smtplib.SMTP_SSL('smtp.qq.com')
    server.login('{}@qq.com'.format(letter_writer), '{}'.format(authorization_code))
    server.sendmail('{}@qq.com'.format(letter_writer), '{}@qq.com'.format(recipients), msg.as_string())
    server.quit()


# 邮件显示的发件人
addressor = "Cody"
# 发件人邮箱
letter_writer = 2093049956
# 邮件主题
motif = "沙雕"
# 邮件内容
content = "你搞好没有啊？"
# 授权码
authorization_code = 'qpfeucotveengbgh'
# 收件人邮箱
recipients = 1259547001

send_email()
