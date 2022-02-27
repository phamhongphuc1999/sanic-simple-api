from sanic_app.config.utils import ServiceType
from sanic_app.factory.controller import controller_factory
from sanic_app.sanic_app import main_app, user_blueprint


def create_routes(**kwargs):
    for key, value in kwargs.items():
        if key == "user" and value:
            controller_factory.create_controller(ServiceType.USER)
            main_app.blueprint(user_blueprint)
