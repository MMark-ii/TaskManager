from app import db
from datetime import datetime

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    theme_prompt = db.Column(db.String(200), nullable=False)
    article_prompt = db.Column(db.String(200), nullable=False)
    image_prompt = db.Column(db.String(200), nullable=False)
    theme_list = db.Column(db.String(200), nullable=False)
    article_list = db.Column(db.String(200), nullable=False)
    schedule = db.Column(db.String(100), nullable=False)
    is_active = db.Column(db.Boolean, default=True)
    platforms = db.relationship('Platform', secondary='task_platform', backref='tasks')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Platform(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

task_platform = db.Table('task_platform',
    db.Column('task_id', db.Integer, db.ForeignKey('task.id'), primary_key=True),
    db.Column('platform_id', db.Integer, db.ForeignKey('platform.id'), primary_key=True)
)
