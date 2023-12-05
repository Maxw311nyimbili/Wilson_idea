import smtplib, ssl

# sending the news to a specified email address
def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "nyimbilimaxwell9@gmail.com"
    password = "ltrpqvpfwrlsrcnu"

    receiver = "nyimbilimaxwell9@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)