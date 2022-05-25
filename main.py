from app import create_app, create_routes, AppConfig

from app.config import EnvironmentType
from app.services.logger_service import app_logger


def run_server(auto_reload=False):
    sanic_app = create_app()
    create_routes(sanic_app, employee=AppConfig.Extension.EMPLOYEE_ROUTER)
    app_logger.info(f"environment: {AppConfig.Environment}")
    sanic_app.run(host=AppConfig.Global.App.HOST, port=AppConfig.Global.App.PORT, auto_reload=auto_reload, debug=False,
                  access_log=True, workers=4)


if __name__ == "__main__":
    _ENV = AppConfig.Environment
    if _ENV == EnvironmentType.DEV_DOCKER:
        run_server()
    elif _ENV == EnvironmentType.DEVELOPMENT:
        run_server(True)
    else:
        app_logger.error(f"Not found {_ENV}, process is stopped")
