from flask import Flask

app = Flask(__name__)

@app.route('/<int:a>')
def index(a):
    return (f'你输入的是{a}')

if __name__ == '__main__':
    app.run()