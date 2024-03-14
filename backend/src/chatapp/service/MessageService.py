from chatapp.database import db_session
from chatapp.models.Message import Message


def save_message(receiver_id, sender_id, content):
    message = Message(receiver_id, sender_id, content)
    db_session.add(message)
    db_session.commit()
    db_session.refresh(message)
    result = message_to_dict(message)
    return result


def find_messages(receiver_id, sender_id):
    sent_messages = Message.query.filter(Message.receiver_id == receiver_id, Message.sender_id == sender_id).all()
    received_messages = Message.query.filter(Message.receiver_id == sender_id, Message.sender_id == receiver_id).all()
    result = []
    for message in sent_messages:
        result.append(message_to_dict(message))
    for message in received_messages:
        result.append(message_to_dict(message))
    return result


def message_to_dict(message: Message):
    result = {'id': message.id,
              'receiver_id': message.receiver_id,
              'sender_id': message.sender_id,
              'content': message.content,
              'timestamp': message.timestamp.ctime()}
    return result
