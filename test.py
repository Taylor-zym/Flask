''''
作者：romtance
时间:2023年01月14日
'''
from flask import Flask,render_template,request
import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

app = Flask(__name__)

def mail(f,toad,content):
    froma = 'yimingzz@hotmail.com'
    password = 'zym02316'
    toad = toad
    content += '\n请查收附件~'
    textapart = MIMEText(content)

    pdf = MIMEApplication(f.read())
    pdf.add_header('Content-Disposition', 'attachment', filename=f.filename)

    m = MIMEMultipart()
    m.attach(textapart)
    m.attach(pdf)

    m['Subject']='来自网页端的文件:%s'%time.asctime()
    sever = smtplib.SMTP("outlook.office365.com", 587)
    sever.ehlo()  # 向邮箱发送SMTP 'ehlo' 命令
    sever.starttls()
    sever.login(froma,password)
    sever.sendmail(froma,toad,m.as_string())
    print('OK')
    sever.quit()

@app.route('/',methods=['POST','GET'])
def index():
    if request.method=='GET':
        return render_template('w.html')
    else:
        file = request.files['file']
        toad = request.form.get('toad')
        content = request.form.get('text')
        content +=' '
        print(toad)
        mail(file,toad,content)
        return '<h1>发送成功至mailto:%s</h1>'%toad
if __name__ == '__main__':
    app.run()