import traceback
import logging
from portfolio.models import Message, engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind = engine)
session = Session()

def create(data):
    try:
        msg = Message(name=data["name"], email=data["email"], subject=data["subject"], message=data["message"])
        session.add(msg)
        session.commit()
        return True, "Successfully saved the message."
    except Exception:
        tb = traceback.format_exc()
        logging.error(tb)
        return False, "Failed to save the message."

def findAll():
    datas = session.query(Message).all()
    return [dict(id=m.id, name=m.name, email=m.email, subject=m.subject, message=m.message) for m in datas]

def findById(id):
    rec = session.query(Message).filter(Message.id == id).first()
    if rec is not None:
        return dict(id=rec.id, name=rec.name, email=rec.email, subject=rec.subject, message=rec.message)

def findByName(name = None):
    datas = session.query(Message).filter(Message.name == name)
    return [dict(id=m.id, name=m.name, email=m.email, subject=m.subject, message=m.message) for m in datas]

def delete(id):
    session.query(Message).filter(Message.id == id).delete()
    session.commit()
    return "Deleted the message."

def filter(params):
    filter = [getattr(Message, key).like(f"%{value}%") for key, value in params.items()]
    datas = session.query(Message).filter(*filter).all()
    return [dict(id=m.id, name=m.name, email=m.email, subject=m.subject, message=m.message) for m in datas]