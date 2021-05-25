import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import os

PATH = os.path.dirname(__file__)

class EmailTools:

    def __init__(self, username, password):
        self.smtp = smtplib.SMTP_SSL('smtp.qq.com:465')
        self.smtp.login(username, password)
        self.msgRoot = MIMEMultipart('related')

    def email_set(self, title, sender, receiver, msgText, msgImage):
        self.msgRoot['Subject'] = title
        self.msgRoot['From'] = sender
        self.msgRoot['To'] = receiver
        self.msgRoot.attach(msgText)
        self.msgRoot.attach(msgImage)

    def __make_email_html(self, tem_name, comp_exe):

        tem_file_path = f"{PATH}/template/{tem_name}"
        with open(tem_file_path, "r+", encoding="utf-8")as file:
            html_tem_text = file.read()
        html_tem_text = html_tem_text.replace("CompanyExecutive", comp_exe)
        msgText = MIMEText(html_tem_text, 'html', 'utf-8')
        image = f"{PATH}/template/sign_.png"
        with open(image, "rb")as img:
            image_content = img.read()
            msgImage = MIMEImage(image_content)
            msgImage.add_header('Content-ID', 'image1')
        return msgText, msgImage

    def email_send(self, title, sender, receiver, tem_name, comp_exe, file=False):
        # 添加 添加附件功能
        msgText, msgImage = self.__make_email_html(tem_name, comp_exe)
        self.email_set(title, sender, receiver, msgText, msgImage)
        self.smtp.sendmail(sender, receiver, self.msgRoot.as_string())


if __name__ == '__main__':
    username = "851500029@qq.com"
    password = "cwafeacaffaubaie"
    title = "To Diversified Marketing Group, LLC, Hot Mask with Best Price !!"
    sender = "851500029@qq.com"
    receiver = "583530925@qq.com"
    app = emailTools(username, password)

    app.email_send(title, sender, receiver)
