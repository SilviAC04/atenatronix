from flask_app import app
from flask import render_template, redirect, session, request, flash
from flask_app.models.product import Product
from flask_app.models.user import User
from flask_app.models.type_of_user import Type_of_user
from flask_app.models.compra import Compra

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
    session["product_id"] = product_id
    this_user = User.get_by_id(data)
    this_user_type = Type_of_user.get_by_id({"id": this_user.user_type_id})
    this_product = Product.get_by_id({"id": product_id})
    return render_template("add_product.html", 
                           this_user=this_user, 
                           this_user_type=this_user_type,
                           this_product=this_product)

@app.route('/save_buy_and_product', methods=['POST'])
def save_buy_and_product():
    if 'user_id' not in session:
        return redirect('/logout')
    if 'product_id' not in session:
        return redirect('/products')
    if 'compra_id' not in session:
        total_compra = 0
        data = {"descripcion":"poner un nombre a la compra",
                "total":total_compra}
        session['compra_id'] = Compra.save(data)
    else:
        compra = Compra.get_by_id({"id":session["compra_id"]})
        total_compra = compra.total
    
    producto = Product.get_by_id({"id":session["product_id"]})
    
    total_compra+=total_compra+producto.precio*float(request.form["cantidad"])
    print("compra total: ",total_compra)
    data_has = {"user_id":session["user_id"],
                "product_id":session["product_id"],
                "cantidad":int(request.form['cantidad']),
                "compra_id":session["compra_id"],
                "oferta_id":1}
    data = {"id":session["compra_id"],
            "descripcion":"poner un nombre a la compra",
            "total":float(total_compra)}
    User.buys_product(data_has)
    Compra.update(data)
    compra_id = session["compra_id"]
    return redirect('/shopping')

@app.route('/shopping/<int:compra_id>')
def myshopping(compra_id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":session["user_id"]
    }
    this_user = User.get_by_id(data)
    this_user_type = Type_of_user.get_by_id({"id": this_user.user_type_id})
    dataq = {'user_id':session['user_id'],
             'compra_id':compra_id}
    mis_compras = Product.get_products_in_order(dataq)
    datos_compra = Compra.get_by_id({'id':compra_id})
    return render_template("shopping_cart.html", this_user=this_user,
                           this_user_type=this_user_type,
                           this_buys = mis_compras,
                           datos_compra = datos_compra)
    
@app.route('/finish_buy', methods=['POST'])
def finish_buy():
    session.pop('compra_id')
    return redirect('/products')
