from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user

from .models import UserBase, User

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/signup')
def signup():
    return render_template('login.html')

@auth.route('/logout')
def logout():
    logout_user()
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post(): 
    login = request.form.get('login')
    password = request.form.get('password') 

    if login in UserBase.logins.keys():
        user=UserBase.logins[login] 
        print(UserBase.logins[login].passwd)
        if password == user.passwd: 
            user_logged_in=User(login,password)
            UserBase.sessions[user_logged_in.id]=user_logged_in
            login_user(user_logged_in) 
            return redirect(url_for('main.index'))

        else: 
            flash('Wrong Password')
            return redirect(url_for('auth.login'))
    else:
        flash('Login is not exists')
        return redirect(url_for('auth.login'))
