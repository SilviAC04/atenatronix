from flask_app import app
from flask import render_template, redirect, session, request, flash
from flask_app.models.product import Product
from flask_app.models.user import User
from flask_app.models.type_of_user import Type_of_user

@app.route('/products')
def show_products():
    if 'user_id' not in session:
        return redirect('/logout')
    # products = Product.get_all()
    products = Product.get_all_product_table()
    return render_template("products.html", this_products = products)

@app.route('/comprar-<int:product_id>')
def confirm_add_product(product_id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":session["user_id"]
    }
    this_user = User.get_by_id(data)
    this_user_type = Type_of_user.get_by_id({"id": this_user.user_type_id})
    this_product = Product.get_by_id({"id": product_id})
    return render_template("add_product.html", 
                           this_user=this_user, 
                           this_user_type=this_user_type,
                           this_product=this_product)