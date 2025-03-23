from app import db

class Platform(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    script_path = db.Column(db.String(200), nullable=False)
