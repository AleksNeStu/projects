"""Flask application run."""
import flask
# from infra.view_modifiers import response
from pypi_org.infra.view_modifiers import response

app = flask.Flask(__name__)

def get_latest_packages():
    return [
        {'name': 'flask', 'version': '1.2.0a'},
        {'name': 'jinja2', 'version': '1.3.0b'},
        {'name': 'passlib', 'version': '1.4.0c'},
    ]

TEST_PACKAGES = get_latest_packages()

@app.route('/')
@response(template_file='home/index.html')
def index():
    return {
        'packages': TEST_PACKAGES
    }
    # return flask.render_template('home/index.html', packages=TEST_PACKAGES)

@app.route('/about')
@response(template_file='home/about.html')
def about():
    return {

    }
    # return flask.render_template('home/about.html')

if __name__ == '__main__':
    app.run(port=5000, debug=True)