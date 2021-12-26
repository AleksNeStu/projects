import flask


app = flask.Flask(__name__)

@app.route('/')
def index():
    return 'Hi bro!'

if __name__ == '__main__':
    app.run(port=5000, debug=True)