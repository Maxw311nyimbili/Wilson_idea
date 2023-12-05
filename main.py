from flask import Flask, render_template, request

import send

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def form():
    if request.method == "GET":
        title = "Thank you"
        return render_template("index.html", title=title)
    elif request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        date = request.form.get("date")
        subject = request.form.get("subject")
        response = ""
        if request.form.get("yes") == "on":
            response = response + "Student wants tutorial session"
        else:
            response = response + "Student does not want tutorial session"
        body = ""
        body = body + "Subject: Alert, new student" + "\n" + \
               name + "\n" + email + "\n" + date.split("T")[0] + \
               "\n" + date.split("T")[1] + "\n" + subject + "\n" + response

        send.send_email(body)
        return render_template("index.html", name=request.form)


if __name__ == "__main__":
    app.run(debug=True)
