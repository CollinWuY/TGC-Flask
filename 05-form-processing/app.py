from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)


@app.route('/')
def home():
    return "home"


@app.route('/booking')
def show_booking_form():
    return render_template('show_booking_form.template.html')


@app.route('/booking', methods=['POST'])
def process_booking_form():
    first_name = request.form.get('first-name')
    last_name = request.form.get('last-name')
    return render_template("say_hello.template.html",
                           fname=first_name, lname=last_name)


# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
