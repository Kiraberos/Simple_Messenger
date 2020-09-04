from datetime import datetime

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/status")
def status():
    return {
        'status': True,
        'time': datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    }


app.run()
