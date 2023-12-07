import base64

from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
import send

from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static\\files'


@app.route("/", methods=["POST", "GET"])
def form():
    if request.method == "GET":
        title = "Thank you"
        return render_template("index.html", title=title)
    elif request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        subject = request.form.get("subject")
        file = request.files['file']
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config['UPLOAD_FOLDER'],
                               secure_filename(file.filename)))

        filename = f"{os.path.abspath(os.path.dirname(__file__))}\\{app.config['UPLOAD_FOLDER']}\\{secure_filename(file.filename)}"

        with open(filename, "rb") as attachment:
            content = attachment.read()

        attachment_package = MIMEBase('application', 'octet-stream')
        attachment_package.set_payload(content)
        encoders.encode_base64(attachment_package)
        attachment_package.add_header('Content-Disposition', "attachment; filename = " + filename)

        # --------------------------------------------

        response = ""
        if request.form.get("yes") == "on":
            date = request.form.get("date")
            response = response + "Student wants tutorial session and would like to meet on: " \
                       + "\n" + date.split('T')[0] + " at " + date.split('T')[1] + "via a Zoom call."
        else:
            response = response + "Student does not want tutorial session"

        body = f"Student name: {name} \nStudent's address: {email} " \
               f"\nSubject: {subject}\n\nNB: {response}"

        msg = MIMEMultipart()
        msg["Subject"] = "Alert, new student"
        msg.attach(MIMEText(body, 'plain'))
        msg.attach(attachment_package)
        text = msg.as_string()

        send.send_email(text)
        message_1 = "Submission was successful!"
        message2 = "The solutions will be sent to your email in space of four days"
        return render_template("index.html", name=message_1, name_1=message2)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
