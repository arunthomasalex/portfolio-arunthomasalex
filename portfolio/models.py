from flask import current_app
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine(current_app.config["SQLALCHEMY_DATABASE_URI"], echo = current_app.config['SHOW_QUERY'])

class Message(Base):
    __tablename__ = 'messages'
    id = Column(Integer, primary_key = True)
    name = Column(String(20), nullable = False)
    email = Column(String(100), nullable = False)
    subject = Column(String(100), nullable = False)
    message = Column(String(500), nullable = False)