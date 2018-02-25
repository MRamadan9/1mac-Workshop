from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def home_page():
    return 'Hello from Falsk :)'

@app.route('/SayHello/<user>')
def say_hello(user):
    return "Hello {}".format(user)

if __name__=='__main__':
	app.run(debug=True)