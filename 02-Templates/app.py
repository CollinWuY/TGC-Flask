from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('hello.template.html')

@app.route('/about/<first_name>/<last_name>')
def about(first_name, last_name):
    # first_name = "Col"
    # last_name = "Wu"
    return render_template('about.template.html', fname=first_name, lname=last_name)

# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)