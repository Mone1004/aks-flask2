import platform
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Server Host : in {}".format(platform.node())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
