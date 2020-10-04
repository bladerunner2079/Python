import config
import smtplib


class EmailAlert(object):
    def __init__(self, subject, msg):
        self.subject = subject
        self.msg = msg

    def send_email(self):
        try:
            server = smtplib.SMTP('smtp.gmail.com:587')
            server.ehlo()
            server.starttls()
            server.login(config.from_email_address, config.password)
            message = 'Subject: {}\n\n{}'.format(self.subject, self.msg)
            server.sendmail(config.from_email_address,
                            config.to_email_address,
                            message)
            server.quit()
            print("Success: Email sent!")
        except:
            print("Email failed to send.")