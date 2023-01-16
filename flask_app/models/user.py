from flask_bcrypt import Bcrypt
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import comic, comment
import re
EMAIL_REGEX = re.compile(
    r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')  # my regex
# bcrypt
bcrypt = Bcrypt(app)
db_name = 'super_social_reader'


class User:
    def __init__(self, data):
        self.id = data['id']
        self.username = data['username']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.comics = []
        self.comments = []

    # CRUD class methods
    @classmethod
    def create_user(cls, data):
        query = """INSERT INTO users
        (username, email, password)
        VALUES (%(username)s,%(email)s,%(password)s);"""
        return connectToMySQL(db_name).query_db(query, data)
    # Grabbing class methods

    @classmethod
    def get_user_by_id(cls, data):
        query = 'SELECT * FROM users WHERE id = %(id)s;'
        result = connectToMySQL(db_name).query_db(query, data)
        if len(result) == 0:
            print('We had trouble grabbing user by id...')
        else:
            print('found and getting user...')
            return cls(result[0])
    @classmethod
    def get_user_by_email(cls, data):
        query = 'SELECT * FROM users WHERE email = %(email)s;'
        result = connectToMySQL(db_name).query_db(query, data)
        if len(result) == 0:
            print('We had trouble grabbing user by email...')
        else:
            print('found and getting user...')
            return cls(result[0])

    # Static Methods
    @staticmethod
    def val_reg(reg_data):
        is_valid = True
        if len(reg_data['username']) < 2:
            flash('*Username must be 2 characters or more!', 'register')
            is_valid = False
        if not EMAIL_REGEX.match(reg_data['email']):
            flash('*Please provide a valid email address', 'register')
            is_valid = False
        email_data = {
            'email': reg_data['email']
        }
        found_user_or_not = User.get_user_by_email(email_data)
        if found_user_or_not != None:
            flash(f'{reg_data["email"]} has already been used', 'register')
            is_valid = False
        if len(reg_data['password']) < 8:
            flash('*Username must be 8 characters or more!', 'register')
            is_valid = False
        if reg_data['password'] != reg_data['confirm_password']:
            flash('*Passwords do not match!', 'register')
            is_valid = False
        return is_valid

    @staticmethod
    def val_login(login_data):
        if not EMAIL_REGEX.match(login_data['email']):
            flash('*Invalid login credentials!', 'login')
            return False
        email_data = {
            'email': login_data['email']
        }
        found_user = User.get_user_by_email(email_data)
        if found_user == None:
            flash('*Invalid login credentials!', 'login')
            return False
        if not bcrypt.check_password_hash(found_user.password, login_data['password']):
            flash('Invalid login credentials!', 'login')
            return False
        return found_user
