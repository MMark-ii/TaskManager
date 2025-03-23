from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user
from .models import User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    # Добавьте реализацию логина
    return render_template('auth/login.html')

@auth_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))