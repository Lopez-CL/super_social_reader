from flask_app import app
from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user, comment
db_name = 'super_social_reader'


class Comic:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.author = data['author']
        self.artist = data['artist']
        self.colorist = data['colorist']
        self.letterer = data['letterer']
        self.status = data['status']
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
        
    @classmethod
    def update_comic(cls,data):
        query = """UPDATE comics SET
        title = %(title)s,
        author = %(author)s, 
        artist = %(artist)s, 
        colorist = %(colorist)s, 
        letterer = %(letterer)s, 
        status = %(status)s, 
        rating = %(rating)s,
        thought = %(thought)s
        WHERE id = %(id)s
        """
        return connectToMySQL(db_name).query_db(query,data)

    @classmethod
    def delete(cls,data):
        query = "DELETE FROM comics WHERE id = %(id)s;"
        return connectToMySQL(db_name).query_db(query, data)

# Grabbing Class Methods

    @classmethod
    # consider conditioning query by status. As comics increase over time, it would shorten the list that we would need to loop through!
    def get_all_comics_with_users(cls):
        query = """SELECT * from comics
        LEFT JOIN users
        ON comics.user_id = users.id;"""
        results = connectToMySQL(db_name).query_db(query)
        all_comics = []
        if len(results) == 0:
            print('Had trouble getting comics...')
            return []
        else:
            for this_comic_dictionary in results:
                this_comic_obj = cls(this_comic_dictionary)
                this_user_dictionary = {
                    'id': this_comic_dictionary['users.id'],
                    'username': this_comic_dictionary['username'],
                    'email': this_comic_dictionary['email'],
                    'password': this_comic_dictionary['password'],
                    'created_at': this_comic_dictionary['users.created_at'],
                    'updated_at': this_comic_dictionary['users.updated_at']
                }
                this_user_obj = user.User(this_user_dictionary)
                this_comic_obj.user = this_user_obj
                all_comics.append(this_comic_obj)
            print(all_comics)
            print(all_comics[0].user.id)
            return all_comics

    @classmethod
    def get_all_session_user_comics(cls, data):
        query = """SELECT * from comics
        LEFT JOIN users
        ON comics.user_id = users.id
        WHERE users.id = %(id)s AND comics.status = 'reading';"""
        results = connectToMySQL(db_name).query_db(query, data)
        all_users_comics = []
        if len(results) == 0:
            print("Had trouble getting the user comics...")
            return []
        else:
            print(results)
            for this_comic_dictionary in results:
                this_comic_obj = cls(this_comic_dictionary)
                print(this_comic_obj)
                this_user_dictionary = {
                    'id': this_comic_dictionary['users.id'],
                    'username': this_comic_dictionary['username'],
                    'email': this_comic_dictionary['email'],
                    'password': this_comic_dictionary['password'],
                    'created_at': this_comic_dictionary['users.created_at'],
                    'updated_at': this_comic_dictionary['users.updated_at']
                }
                this_user_obj = user.User(this_user_dictionary)
                this_comic_obj.user = this_user_obj
                all_users_comics.append(this_comic_obj)
            print(all_users_comics[0].title)
            return all_users_comics

    @classmethod
    def grab_comic_by_id(cls, data):
        query = "SELECT * FROM comics where id = %(id)s;"
        result = connectToMySQL(db_name).query_db(query, data)
        if len(result[0]) == 0:
            print('had trouble getting comic...')
        else:
            print('found and getting comic!')
            return cls(result[0])

    @classmethod
    def grab_comic_by_id_with_user(cls, data):
        query = """SELECT * FROM comics 
        LEFT JOIN users
        ON comics.user_id = users.id
        WHERE comics.id = %(id)s;"""
        result = connectToMySQL(db_name).query_db(query, data)
        print('had trouble getting comic...')
        print('found and getting comic!')
        print(result)
        for this_comic_dictionary in result:
            this_comic_obj = cls(this_comic_dictionary)
            print(this_comic_obj)
            this_user_dictionary = {
                'id': this_comic_dictionary['users.id'],
                'username': this_comic_dictionary['username'],
                'email': this_comic_dictionary['email'],
                'password': this_comic_dictionary['password'],
                'created_at': this_comic_dictionary['users.created_at'],
                'updated_at': this_comic_dictionary['users.updated_at']
            }
            this_user_obj = user.User(this_user_dictionary)
            this_comic_obj.user = this_user_obj
        print(this_comic_obj)
        return this_comic_obj

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
