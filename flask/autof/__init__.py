from flask import Flask
from flask_login import LoginManager
from .models import UserBase

print(UserBase.sessions)

def create_app():
    app=Flask(__name__)
    app.secret_key='slkdncskjdfbvjdhfbvjdsbc'

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)


    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    @login_manager.user_loader
    def load_user(user_id):

        return UserBase.sessions[user_id]


    from .files import files as files_blueprint
    app.register_blueprint(files_blueprint)

    #from .autoindex import auto_bp
    #app.register_blueprint(auto_bp, url_prefix='/file')

    return app


