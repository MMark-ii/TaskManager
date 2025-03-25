# app/__init__.py

from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from datetime import datetime
import logging

db = SQLAlchemy()
login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    from .auth.models import User
    return User.query.get(int(user_id))

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')
    
    db.init_app(app)
    login_manager.init_app(app)
    
    @app.route('/')
    def index():
        return redirect(url_for('auth.login'))
    
    @app.route('/favicon.ico')
    def favicon():
        return app.send_static_file('favicon.ico'), 200, {'Content-Type': 'image/x-icon'}
    
    @app.errorhandler(Exception)
    def handle_exception(e):
        app.logger.error(f"Error: {str(e)}")
        return str(e), 500
    
    with app.app_context():
        db.create_all()
        from .auth.routes import auth_bp
        from .tasks.routes import tasks_bp
        from .platforms.routes import platforms_bp
        
        app.register_blueprint(auth_bp)
        app.register_blueprint(tasks_bp, url_prefix='/tasks')
        app.register_blueprint(platforms_bp)
    
    app.logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler('app.log')
    app.logger.addHandler(handler)
    
    return app
