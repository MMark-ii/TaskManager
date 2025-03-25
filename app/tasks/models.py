from app import db
from datetime import datetime

class Platform(db.Model):
    __tablename__ = 'platforms'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Связь с задачами (один-ко-многим)
    tasks = db.relationship('Task', back_populates='platform', cascade='all, delete-orphan')

    def __repr__(self):
        return f'<Platform {self.name}>'

class Task(db.Model):
    __tablename__ = 'tasks'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text)
    theme_prompt = db.Column(db.String(200), nullable=True)
    article_prompt = db.Column(db.Text, nullable=True)  # Новое поле
    image_prompt = db.Column(db.Text, nullable=True)  # Новое поле
    is_completed = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Связь с платформой
    platform_id = db.Column(db.Integer, db.ForeignKey('platforms.id'))
    platform = db.relationship('Platform', back_populates='tasks')
    
    def __repr__(self):
        return f'<Task {self.title}>'
