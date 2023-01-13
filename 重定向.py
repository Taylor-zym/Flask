''''
作者：romtance
时间:2023年01月13日
'''
from flask import Flask,url_for

app = Flask(__name__)

@app.route('/admin')
def admin():
    return 'Welcome Admin'

@app.route('/user')
def user():
    return 'Welcome User!'

@app.route('/<string:name>')
def check(name):
    if name == 'User':
        app.url_for('user')
    elif name=='admin':
        app.url_for('admin')
    else:
        return 'Error Vistor'

if __name__ == '__main__':
    app.run()
