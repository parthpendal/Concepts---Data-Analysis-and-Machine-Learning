from flask import Flask

#WSGI application
app = Flask(__name__)

@app.route('/')
def hello_world():  # put application's code here
    return 'This is Parth flask application. please subscribe. Please'

@app.route('/members')
def members():
    return 'Welcome members'

if __name__ == '__main__':
    app.run(debug=True)