from sanic import Sanic
from sanic_app.config import GlobalAppConfig
from sanic_app.controllers.employee_controller import employee_blueprint

main_app = Sanic(GlobalAppConfig.AppConfig.APP_NAME)


def create_routes(**kwargs):
    for key, value in kwargs.items():
        if key == "employee" and value:
            main_app.blueprint(employee_blueprint)
