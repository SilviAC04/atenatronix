from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Type_of_user:
    db = 'atenatronixdb'
    def __init__(self, data):
        self.id = data["id"]
        self.description = data["description"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        
    @classmethod
    def save(cls,data):
        query = "INSERT INTO users_types (description) VALUES(%(description)s)"
        return connectToMySQL(cls.db).query_db(query,data)
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users_types;"
        results = connectToMySQL(cls.db).query_db(query)
        users = []
        for row in results:
            users.append( cls(row))
        return users
    
    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM users_types WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        print(results)
        return cls(results[0])
