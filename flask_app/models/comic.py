from flask_app import app
from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user, comment
db_name = 'super_social_reader'


class Comic:
    def __init__(self, data):
        self.id = data['id']
        self.author = data['author']
        self.artist = data['artist']
        self.colorist = data['colorist']
        self.letterer = data['letterer']
        self.rating = data['rating']
        self.thought = data['thought']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user = None

# CRUD Class methods

    @classmethod
    def save(cls, data):
        query = """INSERT INTO comics
        (user_id, title, author, artist, colorist, letterer, status, rating,thought)
        VALUES (%(user_id)s,%(title)s,%(author)s,%(artist)s,%(colorist)s,%(letterer)s,%(status)s,%(rating)s,%(thought)s);"""
        print('Creating comic!')
        return connectToMySQL(db_name).query_db(query, data)

#Grabbing Class Methods


# Static Validations

    @staticmethod
    def val_comic(comic_data):
        is_valid = True
        if len(comic_data['title']) <= 0:
            flash('*Title required. Must provide title of comic', 'comic')
            is_valid = False
        if len(comic_data['author']) <= 0:
            flash('*Author required. Must enter name(s)', 'comic')
            is_valid = False
        if len(comic_data['artist']) <= 0:
            flash('*Artist required. Must enter name(s)', 'comic')
            is_valid = False
        if len(comic_data['colorist']) <= 0:
            flash('*Colorist required. Must enter name(s)', 'comic')
            is_valid = False
        if len(comic_data['letterer']) <= 0:
            flash('*Letterer required. Must enter name(s)', 'comic')
            is_valid = False
        if len(comic_data['status']) <= 0:
            flash('*You must indicate reading status', 'comic')
            is_valid = False
        return is_valid
