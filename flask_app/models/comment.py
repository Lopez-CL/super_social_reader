from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user,comic
db_name = 'Super_social_reader'

class Comment():
    def __init__(self,data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.comic_id = data['comic_id']
        self.content = data['content']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.sender = None
# Class methods
    # R MEthods
    @classmethod
    def get_comments_by_comic_id(cls,data):
        query = """
        SELECT * FROM comments
        LEFT JOIN users AS sender
        ON comments.user_id = sender.id
        WHERE comments.comic_id = %(id)s
        ORDER BY comments.created_at;
        """
        results = connectToMySQL(db_name).query_db(query,data)
        all_comments = []
        # if results == None:
        #     print('had trouble getting comments')
        #     return None
        for dictionary in results:
            this_comment_obj = cls(dictionary)
            this_sender_dictionary = {
                'id': dictionary['sender.id'],
                'username': dictionary['username'],
                'email': dictionary['email'],
                'password': dictionary['password'],
                'created_at': dictionary['sender.created_at'],
                'updated_at': dictionary['sender.updated_at'],
                'file_name': dictionary['file_name']
            }
            this_sender_obj = user.User(this_sender_dictionary)
            this_comment_obj.sender = (this_sender_obj)
            all_comments.append(this_comment_obj)
        # print(all_comments[0].content)
        return all_comments




    #C(UD) methods
    @classmethod
    def save(cls,data):
        query = """INSERT INTO comments
        (user_id, comic_id, content)
        VALUES (%(user_id)s,%(comic_id)s,%(content)s);"""
        connectToMySQL(db_name).query_db(query,data)
# Static methods
    @staticmethod
    def val_comment(comment_data):
        is_valid = True
        if len(comment_data['content']) < 2:
            flash('*Comment must be two characters or more', 'comment')
            is_valid = False
            print(is_valid)
        return is_valid
