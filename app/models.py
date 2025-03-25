from datetime import datetime
from app import db  # Импортируйте экземпляр SQLAlchemy из app/__init__.py

# Ассоциативная таблица для связи many-to-many между Task и Platform
task_platform = db.Table(
    'task_platform',
    db.Column('task_id', db.Integer, db.ForeignKey('task.id'), primary_key=True),
    db.Column('platform_id', db.Integer, db.ForeignKey('platform.id'), primary_key=True)
)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    theme_prompt = db.Column(db.String(200))
    article_prompt = db.Column(db.String(200))
    image_prompt = db.Column(db.String(200))
    theme_list = db.Column(db.String(200))
    article_list = db.Column(db.String(200))
    platforms = db.Column(db.JSON)
    schedule = db.Column(db.String(50))
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    platforms = db.relationship('Platform', secondary=task_platform, backref='tasks')
    

class Platform(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    script_path = db.Column(db.String(200), nullable=False)