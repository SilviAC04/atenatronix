from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

# Regex 2 validate email
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    db = 'atenatronixdb'
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.password = data["password"]
        self.birthday = data["birthday"]
        self.cedula_ruc = data["cedula_ruc"]
        self.user_type_id = int(data["user_type_id"])
        self.empresa_id = int(data["empresa_id"])
        self.direccion_id = data["direccion_id"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.orders = []
        self.offers = []
    
    @classmethod
    def save(cls,data):
        query = "INSERT INTO users (first_name,last_name,email,password, birthday, cedula_ruc, user_type_id, empresa_id, direccion_id) VALUES(%(first_name)s,%(last_name)s,%(email)s,%(password)s, %(birthday)s, %(cedula_ruc)s, %(user_type_id)s, %(empresa_id)s, %(direccion_id)s)"
        return connectToMySQL(cls.db).query_db(query,data)
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(cls.db).query_db(query)
        users = []
        for row in results:
            users.append( cls(row))
        return users
    
    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        print(results)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        print(results)
        return cls(results[0])

    @staticmethod
    def validate_register(user):
        is_valid = True
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(User.db).query_db(query,user)
        if len(results) >= 1:
            flash("Email ya existe.","register")
            is_valid=False
        if not EMAIL_REGEX.match(user['email']):
            flash("Email no es valido","register")
            is_valid=False
        if len(user['first_name']) < 3:
            flash("El nombre debe tener al menos 3 caracteres","register")
            is_valid= False
        if len(user['last_name']) < 3:
            flash("El apellido debe tener al menos 3 caracteres","register")
            is_valid= False
        if len(user['password']) <= 8:
            flash("La contraseña debe tener al menos 8 caracteres","register")
            is_valid= False
        if user['password'] != user['confirm']:
            flash("Las contraseñas no coinciden","register")
        return is_valid

