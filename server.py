import time
from datetime import datetime

from flask import Flask, request

app = Flask(__name__)
messages = [
    {"username": "Jack", "text": "Hello", "time": time.time()},
    {"username": "Mary", "text": "Hi", "time": time.time()},
]

users = {
    'Jack': '12345',
    'Mary': '54321'
}


@app.route("/")
def hello_view():
    return "<h1>Welcome to Python messenger</h1>"


@app.route("/status")
def status_view():
    return {
        'status': True,
        'time': datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    }


@app.route("/messages")
def messages_view():
    """
    Receiving messages "after" event
    input: after
    output: {
        [
            {"username": "str, "text": str, "time": float},
            ...
        ]
    }

    """
    after = float(request.args['after'])

    new_messages = [message for message in messages if message['time'] > after]
    return {"messages": messages}


@app.route("/send", methods=['POST'])
def send_view():
    """
    Sending messages
    input: {
        "username": str,
        "password": str,
        "text": str
    }
    output{"ok": True}

    """
    data = request.json
    password = data["password"]
    username = data["username"]

    if username not in users or users[username] != password:
        return {"ok": False}

    text = data["text"]

    messages.append({"username": username, "text": text, "time": time.time()})

    return {'ok': True}


@app.route("/auth", methods=['POST'])
def auth_view():
    """
    Authorise users or invalid password.
    Sending messages
    input: {
        "username": str,
        "password": str,
    }
    output{"ok": bool}

    """
    data = request.json
    password = data["password"]
    username = data["username"]

    if username not in users:
        users[username] = password
        return {"ok": True}
    elif users[username] == password:
        return {"ok": True}
    else:
        return {"ok": False}


app.run()
