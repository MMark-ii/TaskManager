import os
from app import create_app, db

app = create_app()

# Явное создание базы данных
with app.app_context():
    db.create_all()
    print("База данных создана.")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)