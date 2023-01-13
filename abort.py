''''
作者：romtance
时间:2023年01月13日
'''
from flask import Flask,abort,render_template,request

app = Flask(__name__)

@app.route('/',methods=['POST',"GET"])
def index():
    if request.method=='GET':
        return render_template('log.html')
    else:
        name = request.form.get('name')
        p = request.form.get('pass')
        if p=='1':
            return f'<h1>欢迎{name},你的密码是{p}</h1>'
        else:return abort(404)

@app.errorhandler(404)
def error404(e):
    print(e)
    return render_template('a404.html')
if __name__ == '__main__':
    app.run()