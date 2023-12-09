import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# --------------------------
# outlook stuff
import win32com.client as win32
import pythoncom
# -----------------------

# if you get this error: (-2147221008, 'CoInitialize has not been called.', None, None)
# close pycharm, run as an administrator, then in the terminal uninstall then install pywin32
# using pip uninstall pywin32 pypiwin32 to uninstall and pip install pywin32 pypiwin32 to install

# SENDING EMAIL TO THROUGH GMAIL
def send_email(username_placeholder, file, body, message):
    if username_placeholder.split("@")[1] == "gmail.com":
        host = "smtp.gmail.com"
        port = 465

        username = "nyimbilimaxwell9@gmail.com"
        password = "ltrpqvpfwrlsrcnu"

        receiver = "nyimbilimaxwell9@gmail.com"
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL(host, port, context=context) as server:
            server.login(username, password)
            server.sendmail(username, receiver, message)
    else:
        send_to_outlook(username_placeholder, file, body)

def user_send_email(useremail, message):
    if useremail.split("@")[1] == "gmail.com":
        host = "smtp.gmail.com"
        port = 465

        msg = MIMEMultipart()
        msg["Subject"] = "Submission was successful"
        msg.attach(MIMEText(message, 'plain'))
        text = msg.as_string()

        username = "nyimbilimaxwell9@gmail.com"
        password = "ltrpqvpfwrlsrcnu"

        receiver = useremail
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL(host, port, context=context) as server:
            server.login(username, password)
            server.sendmail(username, receiver, text)
    else:
        user_send_to_outlook(useremail, message)
# SENDING EMAIL THROUGH OUTLOOK
# construction of outlook application instance--------------------
def send_to_outlook(user_name, file, body):
    try:
        pythoncom.CoInitialize()

        olApp = win32.Dispatch('Outlook.Application')
        olNS = olApp.GetNameSpace('MAPI')

        # construct the email item object
        mailItem = olApp.CreateItem(0)
        mailItem.Subject = "Submission was successful"
        mailItem.BodyFormat = 1  # Plain text
        mailItem.Body = body
        mailItem.To = user_name
        mailItem.Attachments.Add(file)
        mailItem._oleobj_.Invoke(*(64209, 0, 8, 0, olNS.Accounts.Item("maxwell.nyimbili@ashesi.edu.gh")))

        # Send the email
        mailItem.Send()

    except Exception as e:
        print(f"An error occurred: {e}")

def user_send_to_outlook(user_name, message):
    try:
        pythoncom.CoInitialize()

        olApp = win32.Dispatch('Outlook.Application')
        olNS = olApp.GetNameSpace('MAPI')

        # construct the email item object
        mailItem = olApp.CreateItem(0)
        mailItem.Subject = "Notification from LoGo Study"
        mailItem.BodyFormat = 1  # Plain text
        mailItem.Body = message
        mailItem.To = user_name
        mailItem._oleobj_.Invoke(*(64209, 0, 8, 0, olNS.Accounts.Item("maxwell.nyimbili@ashesi.edu.gh")))

        # Send the email
        mailItem.Send()

    except Exception as e:
        print(f"An error occurred: {e}")
# # ----------------------------------

