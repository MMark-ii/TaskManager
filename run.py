import os
from app import create_app, db

app = create_app()

# Проверка существования базы данных
db_path = os.path.join(os.path.dirname(__file__), 'site.db')
if not os.path.exists(db_path):
    with app.app_context():
        db.create_all()
        print("База данных создана.")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)