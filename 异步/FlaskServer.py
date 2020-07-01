# coding:utf-8

from flask import Flask, render_template
from time import sleep

app = Flask(__name__)


@app.route('/hui')
def index():
    sleep(2)
    return render_template('test.html')


@app.route('/index')
def index2():
    sleep(2)
    return render_template('test.html')


@app.route('/bobo')
def index3():
    sleep(2)
    return render_template('test.html')


if __name__ == '__main__':
    app.run(debug=True)
