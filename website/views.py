from flask import Blueprint, redirect, render_template, request, flash, jsonify, url_for
from flask_login import login_required, current_user
from .models import *
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/')
@login_required
def index():
    books = Book.query.all()
    return render_template('home.html', books=books)


@views.route('/add/', methods=['POST'])
def insert_book():
    if request.method == "POST":
        book = Book(title=request.form.get('title'),
                    author=request.form.get('author'),
                    price=request.form.get('price'))
        db.session.add(book)
        db.session.commit()
        flash("Book added successfully")
        return redirect(url_for('views.index'))


@views.route('/update/', methods=['POST'])
def update():
    if request.method == "POST":
        my_data = Book.query.get(request.form.get('id'))

        my_data.title = request.form['title']
        my_data.author = request.form['author']
        my_data.price = request.form['price']

        db.session.commit()
        flash("Book is updated")
        return redirect(url_for('views.index'))


@views.route('/delete/<id>/', methods=['GET', 'POST'])
def delete(id):
    my_data = Book.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Book is deleted")
    return redirect(url_for('views.index'))