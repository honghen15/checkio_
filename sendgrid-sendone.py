import sendgrid
from sendgrid.helpers.mail import Email,  Mail, Content

API_KEY = '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'
#SUBJECT = 'Welcome'
#BODY = 'd'

sg = sendgrid.SendGridAPIClient(apikey=API_KEY)

def send_email(email, name):
    from_email = Email("test@example.com")
    to_email = Email(email)
    subject = "Welcome"
    #content = Content("text/plain", "and easy to do anywhere, even with Python")
    content = Content("text/plain", "Hi "+ name )
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    send_email('somebody@gmail.com', 'Some Body')
    print('Done')
