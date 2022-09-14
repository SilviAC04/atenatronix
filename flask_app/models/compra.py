from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Compra:
    db = 'atenatronixdb'
    def __init__(self, data):
        self.id = data["id"]
        self.descripcion = data["descripcion"]
        self.total = data["total"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
    
    @classmethod
    def save(cls,data):
        query = "INSERT INTO compras (descripcion, total) VALUES(%(descripcion)s, %(total)s)"
        return connectToMySQL(cls.db).query_db(query,data)
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM compras;"
        results = connectToMySQL(cls.db).query_db(query)
        users = []
        for row in results:
            users.append( cls(row))
        return users
    
    @classmethod
    def get_by_user_id(cls,data):
        query = """
        select compras.id, compras.descripcion, compras.total from compras
        left join users_has_products on compras.id = users_has_products.compra_id
        left join users on users_has_products.user_id = users.id
        where users.id = %(id)s;
        """
        results = connectToMySQL(cls.db).query_db(query,data)
        return results


    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM compras WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        print(results)
        return cls(results[0])
    
    @classmethod
    def update(cls, data):
        query = "UPDATE compras SET descripcion=%(descripcion)s, total=%(total)s, updated_at=NOW() WHERE id=%(id)s;"
        return connectToMySQL(cls.db).query_db(query, data)

    # @staticmethod
    # def validate_register(user):
    #     is_valid = True
    #     query = "SELECT * FROM users WHERE email = %(email)s;"
    #     results = connectToMySQL(User.db).query_db(query,user)
    #     if len(results) >= 1:
    #         flash("Email ya existe.","register")
    #         is_valid=False
    #     if not EMAIL_REGEX.match(user['email']):
    #         flash("Email no es valido","register")
    #         is_valid=False
    #     if len(user['first_name']) < 3:
    #         flash("El nombre debe tener al menos 3 caracteres","register")
    #         is_valid= False
    #     if len(user['last_name']) < 3:
    #         flash("El apellido debe tener al menos 3 caracteres","register")
    #         is_valid= False
    #     if len(user['password']) <= 8:
    #         flash("La contraseña debe tener al menos 8 caracteres","register")
    #         is_valid= False
    #     if user['password'] != user['confirm']:
    #         flash("Las contraseñas no coinciden","register")
    #     return is_valid

