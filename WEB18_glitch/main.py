import os
from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return 'privet ot flask'


if __name__ == '__main__':
    port = int(os.environ.get('port', 8080))
    app.run(host='0.0.0.0', port=port)
