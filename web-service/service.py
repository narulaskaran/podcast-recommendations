from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/<category>')
def sample_endpoint(category):
    return 'Fetching podcasts related to {}'.format(category)