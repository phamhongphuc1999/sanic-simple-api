from sanic import Sanic, Blueprint

from sanic_app.config import GlobalAppConfig

user_blueprint = Blueprint("user_blueprint")

main_app = Sanic(GlobalAppConfig.AppConfig.APP_NAME)


def create_routes(**kwargs):
    for key, value in kwargs.items():
        if key == "user" and value:
            main_app.blueprint(user_blueprint)
