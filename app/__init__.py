from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///minimercado.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = 'super_secret_key'

    db.init_app(app)  # Inicializa SQLAlchemy con la app
    login_manager.init_app(app)
    login_manager.login_view = 'main.login'

    from .controllers import routes
    app.register_blueprint(routes.bp)

    with app.app_context():
        db.create_all()  # Crea las tablas en la base de datos

    return app

@login_manager.user_loader
def load_user(user_id):
    from .models.models import User
    return User.query.get(int(user_id))
