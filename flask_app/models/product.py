from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

# Regex 2 validate email
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Product:
    db = 'atenatronixdb'
    def __init__(self, data):
        self.id = data["id"]
        self.codigo_fabricante = data["codigo_fabricante"]
        self.descripcion = data["descripcion"]
        self.precio = data["precio"]
        self.stock = data["stock"]
        self.product_type_id = data["product_type_id"]
        self.fabricante_id = data["fabricante_id"]
        self.empresa_id = int(data["empresa_id"])
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        
    @classmethod
    def save(cls,data):
        query = "INSERT INTO products (codigo_fabricante, descripcion, precio, stock, product_type_id, fabricante_id, empresa_id) VALUES (%(codigo_fabricante)s,%(descripcion)s,%(precio)s, %(stock)s, %(product_type_id)s, %(fabricante_id)s, %(empresa_id)s)"
        return connectToMySQL(cls.db).query_db(query,data)
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM products;"
        results = connectToMySQL(cls.db).query_db(query)
        users = []
        for row in results:
            users.append( cls(row))
        return users
    
    @classmethod
    def get_all_product_table(cls):
        query = """
            select products.id, product_types.descripcion as categoria, products.descripcion, products.precio from products 
            left join product_types on products.product_type_id=product_types.id;
        """
        results = connectToMySQL(cls.db).query_db(query)
        # products = []
        # print(results)
        # for row in results:
        #     products.append(cls(row))
        return results
    
    # @classmethod
    # def get_by_email(cls,data):
    #     query = "SELECT * FROM users WHERE email = %(email)s;"
    #     results = connectToMySQL(cls.db).query_db(query,data)
    #     print(results)
    #     if len(results) < 1:
    #         return False
    #     return cls(results[0])

    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM products WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        print(results)
        return cls(results[0])

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

