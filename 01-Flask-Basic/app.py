from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return ("<h1>Hello World</h1><p>It's a beautiful day in Singapore")

@app.route('/about-me')
def about_us():
    return "About Me"

# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)