from flask import Flask
from flask import request
from flask_cors import CORS
from flask_socketio import SocketIO

from chatapp.database import init_db
from chatapp.service import MessageService

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")
init_db()


@app.route("/message", methods=['POST'])
def post_message():
    data = request.get_json()
    receiver: int = data["receiver_id"]
    sender: int = data["sender_id"]
    content: str = data["content"]

    message = MessageService.save_message(receiver, sender, content)
    socketio.emit('new-message', message)
    return message


@app.route("/message")
def get_message():
    receiver_id = request.args.get("receiver_id")
    sender_id = request.args.get("sender_id")

    result = MessageService.find_messages(receiver_id, sender_id)
    return result
