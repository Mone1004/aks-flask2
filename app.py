import platform
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    sumtest=sum(range(10000000))
    return "Server Host : in {}, sum = {}".format(platform.node(),sumtest)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
