from flask import Flask

# Импортируем блюпринт
from main.views import main_blueprint
from candidates.views import candidates_blueprint

# Создаем экземпляр Flask
app = Flask(__name__)

# регистрируем первый блюпринт
app.register_blueprint(main_blueprint)
app.register_blueprint(candidates_blueprint)

if __name__ == '__main__':
    app.run()
