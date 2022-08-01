from django.apps import AppConfig
from django.core.mail import EmailMessage

class QqemailConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'qqemail'

class QqemailUtils:
    def email_html_attachment(self, subject, html_content, to, attachment_path):
        msg = EmailMessage(subject, html_content, "1032010805@qq.com", [to], bcc=["18310401860@163.com"])
        msg.attach_file(attachment_path)
        msg.content_subtype = "html"  # Main content is now text/html
        msg.send()
        print("发送成功")

subject = "test"
html_content = "<h1>test</h1>"
to = "1032010805@qq.com"
qq_email_utils = QqemailUtils()
qq_email_utils.email_html_attachment(subject, html_content, to, "C:\\Users\\HP\\Downloads\\评分标准_106963718.docx")