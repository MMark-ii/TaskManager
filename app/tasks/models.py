from app import db
from datetime import datetime

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
