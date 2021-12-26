import flask


app = flask.Flask(__name__)

@app.route('/')
def index():
    return 'Hi bro!'

app.run()