from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    from .auth.models import User  # Переместите импорт сюда
    return User.query.get(int(user_id))

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')
    
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
