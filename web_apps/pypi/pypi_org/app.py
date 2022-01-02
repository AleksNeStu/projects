"""Flask application run."""
import flask


app = flask.Flask(__name__)

def get_latest_packages():
    return [
        {'name': 'flask', 'version': '1.2.0a'},
        {'name': 'jinja2', 'version': '1.3.0b'},
        {'name': 'passlib', 'version': '1.4.0c'},
    ]

@app.route('/')
def index():
    test_packages = get_latest_packages()
    return flask.render_template('index.html', packages=test_packages)

if __name__ == '__main__':
    app.run(port=5000, debug=True)