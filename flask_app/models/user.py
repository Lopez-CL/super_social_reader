from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import comic, comment
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') #my regex
#bcrypt
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
db_name = 'super_social_reader'

class User:
    def __init__(self,data):
        self.id = data['id']
        self.username = data['username']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.comics = []
        self.comments = []
    
    #CRUD class methods
    @classmethod
    def create_user(cls,data):
        query = """INSERT INTO users
        username, email, password
        VALUES(%(username)s,%(email)s,%(password)s)"""
        return connectToMySQL(db_name).query_db(query,data)
    #Grabbing class methods

    @classmethod
    def get_user_by_id(cls,data):
        query =

    #Static Methods