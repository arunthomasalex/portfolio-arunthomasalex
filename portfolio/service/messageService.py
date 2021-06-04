import traceback
import logging
from portfolio.models import Message, engine

def create(data):
    try:
        insert = Message.insert().values(name=data["name"], email=data["email"], subject=data["subject"], message=data["message"])
        engine.connect().execute(insert)
        return True, "Successfully inserted into database."
    except Exception:
        tb = traceback.format_exc()
        logging.error(tb)
        return False, "Failed to insert into database."

def findAll():
    select = Message.select()
    datas = engine.connect().execute(select)
    return [dict(id=m.id, name=m.name, email=m.email, subject=m.subject, message=m.message) for m in datas]

def findById(id):
    select = Message.select().where(Message.c.id == id)
    data = engine.connect().execute(select)
    return data.fetchone()

def findByName(name = None):
    select = Message.select().where(Message.c.name == name)
    datas = engine.connect().execute(select)
    return [dict(id=m.id, name=m.name, email=m.email, subject=m.subject, message=m.message) for m in datas]

def delete(id):
    delete = Message.delete().where(Message.c.id == id)
    engine.connect().execute(delete)
    return dict(message="Deleted the record.")