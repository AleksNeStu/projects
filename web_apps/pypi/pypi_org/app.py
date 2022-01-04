"""Flask application run."""
import flask


app = flask.Flask(__name__)

def get_latest_packages():
    return [
        {'name': 'flask', 'version': '1.2.0a'},
        {'name': 'jinja2', 'version': '1.3.0b'},
        {'name': 'passlib', 'version': '1.4.0c'},
    ]

TEST_PACKAGES = get_latest_packages()

@app.route('/')
def index():
    return flask.render_template('home/index.html', packages=TEST_PACKAGES)

@app.route('/about')
def about():
    return flask.render_template('home/about.html')

if __name__ == '__main__':
    app.run(port=5000, debug=True)