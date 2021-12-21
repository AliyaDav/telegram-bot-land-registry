# from . import db
import pymongo
import mongoengine
from mongoengine import *


class User(Document):
    email = StringField(required=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)


class User(db.Model):
	# Defines the Table Name user
	__tablename__ = "user"

	# Makes three columns into the table id, name, email
	_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String(100), nullable=False)
	email = db.Column(db.String(100), nullable=False)

	# A constructor function where we will pass the name and email of a user and it gets add as a new entry in the table.
	def __init__(self, data):
        
        self.name = data['First']
        self.surname = data['Last']
        self.gender = data['gender']
        self.docType = data['docType']
        self.docNumber = data['docNumber']
        self.codice = data['codice']
        self.street = data['street']
        self.city = data['city']
        self.region = data['region']
        self.postalCode = data['postalCode']
        # self.country = data['country'] # wont work becasue of selection menu 
        self.houseType = data['houseType']
        self.numFloor = data['numFloor']
        self.propSize = data['propSize']

    def get_user_info(self):
        return {
            
        }

    def get_property_info(sefl):
        return {

        }

    
    def __repr__(self):
        return '<User {}>'.format(self.username)

    # def details(self):
    #     return {
    #         'name': self.name,
    #         'email': self.email,
    #     }
        
    # def insert(self):
    #     db.session.add(self)
    #     db.session.commit()
    # def delete(self):
    #     db.session.delete(self)
    #     db.session.commit()
    # def update(self):
    #     db.session.commit()

# def setup_db(app):
#     '''  
#     binds a flask application and a SQLAlchemy service
#     '''
#     db.app = app
#     db.init_app(app)

# def db_drop_and_create_all():
#     '''
#     drops the database tables and starts fresh.
#     can be used to initialize a clean database
#     '''
#     db.drop_all()
#     db.create_all()
#     return
