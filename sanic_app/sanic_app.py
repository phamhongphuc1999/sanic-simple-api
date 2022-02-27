from sanic import Sanic
from sanic_app.config import GlobalAppConfig
from sanic_app.controllers.user_controller import user_blueprint

main_app = Sanic(GlobalAppConfig.AppConfig.APP_NAME)


def create_routes(**kwargs):
    for key, value in kwargs.items():
        if key == "user" and value:
            main_app.blueprint(user_blueprint)
