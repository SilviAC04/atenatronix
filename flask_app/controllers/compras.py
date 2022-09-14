from flask_app import app
from flask import render_template, redirect, session, request, flash
from flask_app.models.product import Product
from flask_app.models.user import User
from flask_app.models.type_of_user import Type_of_user
from flask_app.models.compra import Compra

@app.route('/shopping')
def mostrar_mis_compras():
    if 'user_id' not in session:
        return redirect('logout')
    
    # all_buys = Compra.get_all()
    data = {
        "id":session["user_id"]
    }
    all_my_buys = Compra.get_by_user_id(data)
    this_user = User.get_by_id(data)
    this_user_type = Type_of_user.get_by_id({"id": this_user.user_type_id})
    return render_template("compras.html", 
                           all_buys=all_my_buys, 
                           this_user=this_user, 
                           this_user_type=this_user_type,)
