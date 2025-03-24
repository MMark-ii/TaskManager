# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  # Создайте экземпляр SQLAlchemy здесь

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    
    db.init_app(app)
    login_manager.init_app(app)
    
    @app.route('/')
    def index():
        return redirect(url_for('auth.login'))
    
    @app.errorhandler(Exception)
    def handle_exception(e):
        return str(e), 500
    
    with app.app_context():
        from .auth.routes import auth_bp
        from .tasks.routes import tasks_bp
        from .platforms.routes import platforms_bp
        
        app.register_blueprint(auth_bp)
        app.register_blueprint(tasks_bp)
        app.register_blueprint(platforms_bp)
        
    return app
