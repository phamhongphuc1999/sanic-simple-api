from sanic import Sanic, Blueprint
from sanic_app.config import GlobalAppConfig

user_blueprint = Blueprint("user_blueprint")
main_app = Sanic(GlobalAppConfig.AppConfig.APP_NAME)
