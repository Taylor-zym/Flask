''''
作者：romtance
时间:2023年01月13日
'''
from flask import Flask,render_template,url_for,request

app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def index():
    if request.method=='GET':
        return render_template("index.html")
    elif request.method=='POST':
        name = request.form["username"]
        print(name)
        return f'<a href="mailto:{name}">{name}</a>'
if __name__ == '__main__':
    app.run()