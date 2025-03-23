from app import db
from datetime import datetime

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    theme_prompt = db.Column(db.Text)
    article_prompt = db.Column(db.Text)
    image_prompt = db.Column(db.Text)
    platforms = db.Column(db.JSON)
    schedule = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
