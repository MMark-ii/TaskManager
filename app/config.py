class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///your_database.db'  # Укажите путь к вашей базе данных
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'your_secret_key'  # Установите секретный ключ