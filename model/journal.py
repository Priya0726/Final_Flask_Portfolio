from random import randrange
from datetime import date
import os, base64
import json

from __init__ import app, db
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash

class Message(db.Model):
    __tablename__ = 'journal_messages'  # table name is plural, class name is singular

    # Define the Message schema with "vars" from object
    id = db.Column(db.Integer, primary_key=True)
    _uid = db.Column(db.String(255), unique=False, nullable=False)
    _message = db.Column(db.Text, nullable=False)
    _date = db.Column(db.DateTime, nullable=False, default=date.today())
    
    # constructor of a Message object, initializes the instance variables within object (self)
    def __init__(self, uid, message, date=date.today()):
        self._uid = uid
        self._message = message
        self._date = date

    # a uid getter method, extracts uid from object
    @property
    def uid(self):
        return self._uid
    
    # a setter function, allows uid to be updated after initial object creation
    @uid.setter
    def is_uid(self, uid):
        self._uid = uid

    # a message getter method, extracts message from object
    @property
    def message(self):
        return self._message
    
    # a setter function, allows message to be updated after initial object creation
    @message.setter
    def message(self, message):
        self._message = message
    
    # a date getter method, extracts date from object
    @property
    def date(self):
        return self._date.strftime('%m-%d-%Y %H:%M:%S')
    
    
    # date should have a setter method as well if needed for updates
    
    # CRUD create/add a new record to the table
    # returns self or None on error
    def create(self):
        try:
            # creates a person object from User(db.Model) class, passes initializers
            db.session.add(self)  # add prepares to persist person object to Users table
            db.session.commit()  # SqlAlchemy "unit of work pattern" requires a manual commit
            return self
        except IntegrityError:
            db.session.remove()
            return None

    # CRUD read converts self to dictionary
    # returns dictionary
    def read(self):
        return {
            "id": self.id,
            "uid": self.uid,
            "message": self.message,
            "date": self.date,
        }

    # CRUD update: updates message content
    # returns self
    def update(self, message):
        self.message = message
        db.session.commit()
        return self

    # CRUD delete: remove self
    # None
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return None
    
def initMessages():
    with app.app_context():
        """Create database and tables"""
        db.create_all()
        
        """Tester data for table"""
        m1 = Message(uid='toby', message='Hi I am going really strong on my mental roadmap')
        messages = [m1]

        """Add message data to the table"""
        for message in messages:
            try:
                message.create()
            except IntegrityError:
                '''fails with bad or duplicate data'''
                db.session.remove()
                print(f"Records exist, duplicate message, or error: {message.uid}")