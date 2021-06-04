import traceback
import logging
from portfolio.models import Message, engine

def create(data):
    try:
        insert = Message.insert().values(name=data["name"], email=data["email"], subject=data["subject"], message=data["message"])
        with engine.connect() as con:
            con.execute(insert)
        return True, "Successfully inserted into database."
    except Exception:
        tb = traceback.format_exc()
        logging.error(tb)
        return False, "Failed to insert into database."

def findAll():
    select = Message.select()
    with engine.connect() as con:
        datas = con.execute(select)
    return [dict(id=m.id, name=m.name, email=m.email, subject=m.subject, message=m.message) for m in datas]

def findById(id):
    select = Message.select().where(Message.c.id == id)
    with engine.connect() as con:
        data = con.execute(select)
    return data.fetchone()

def findByName(name = None):
    select = Message.select().where(Message.c.name == name)
    with engine.connect() as con:
        datas = con.execute(select)
    return [dict(id=m.id, name=m.name, email=m.email, subject=m.subject, message=m.message) for m in datas]

def delete(id):
    delete = Message.delete().where(Message.c.id == id)
    with engine.connect() as con:
        con.execute(delete)
    return dict(message="Deleted the record.")