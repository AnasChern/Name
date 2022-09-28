from flask import Flask
from waitress import serve

app = Flask(__name__)
STUDENTID = 26

@app.route('/')
def hello_world1():
    return "Hello World 26___"

@app.route(f'/api/v1/hello-world{STUDENTID}'.format(STUDENTID))
def hello_world():
    return "Hello World 26"


if __name__ == 'main':
    app.run(debug=True)

serve(app)