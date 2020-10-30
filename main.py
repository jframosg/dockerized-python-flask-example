import os
from flask import Flask


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/test')
def test():
    return 'This is the test service'

@app.route('/help')
def help():
    return 'This is the help service'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

