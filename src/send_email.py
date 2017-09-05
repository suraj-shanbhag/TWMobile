import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

import pdfkit
from pdfkit.configuration import Configuration


class EmailClient(object):
    def __init__(self, user_id, password, host="smtp.gmail.com", port=587):
        self.port = port
        self.host = host
        self.password = password
        self.user_id = user_id

    def _get_mail_client(self):
        mail_client = smtplib.SMTP(host=self.host, port=self.port)
        mail_client.ehlo()
        mail_client.starttls()
        mail_client.login(user=self.user_id, password=self.password)
        return mail_client

    def send_ticket(self, ticket_info):
        mail_client = self._get_mail_client()
        message = self._get_ticket(ticket_info)
        mail_client.sendmail(from_addr=self.user_id, to_addrs=ticket_info['email'], msg=message)
        mail_client.quit()

    def _get_ticket(self, ticket_info):
        message = MIMEMultipart('alternative')
        message['Subject'] = "Train Ticket"
        message['From'] = "Travel Agent"
        message['To'] = ticket_info['email']
        attachment = self._get_ticket_attachment()
        message.attach(attachment)
        return message.as_string()

    def _get_ticket_attachment(self):
        configuration = Configuration(wkhtmltopdf='/app/bin/wkhtmltopdf')
        pdf = pdfkit.from_string("Hello There", False, configuration=configuration)
        attachment = MIMEBase('application', 'octet-stream')
        attachment.set_payload(pdf)
        encoders.encode_base64(attachment)
        attachment.add_header('Content-Disposition', "attachment; filename= Ticket")
        return attachment
