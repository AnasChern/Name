from flask import Flask
from waitress import serve

app = Flask('name')

@app.route('/')
def hello_world1():
    return "Hello World 14___"

@app.route('/api/v1/hello-world14')
def hello_world():
    return "Hello World 14"


if __name__ == 'main':
    app.run(debug=True)

serve(app)