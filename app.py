from flask import Flask, render_template, request
import smtplib

MY_EMAIL = "dchirag5050@gmail.com"

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/contact", methods=["POST"])
def contact():
    name = request.form["name"]
    email = request.form["email"]
    message = request.form["message"]
    send_email(name, email, message)
    return f"<h1>Successfully Message is sent.\nWill reach you back ASAP.</h1>"


def send_email(name, email, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nMessage: {message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, password="uldahsssgfnsptkw")
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=email_message)


if __name__ == "__main__":
    app.run(debug=True)