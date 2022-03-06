from sanic_app.config import EnvironmentType, GlobalAppConfig
from sanic_app.config.extension_config import EMPLOYEE_ROUTER
from sanic_app.factory.database import database_factory
from sanic_app.sanic_app import main_app, create_routes
from sanic_app.services.options import setup_options
from sanic_app.services.sanic_cors import add_cors_headers
from sanic_app.services.utils import get_environment


def run_server(auto_reload=False):
    create_routes(employee=EMPLOYEE_ROUTER)
    main_app.register_listener(setup_options, "before_server_start")
    main_app.register_middleware(add_cors_headers, "response")
    main_app.run(host=GlobalAppConfig.AppConfig.APP_HOST, port=GlobalAppConfig.AppConfig.APP_PORT,
                 auto_reload=auto_reload, debug=True, access_log=True)


if __name__ == "__main__":
    _ENV = get_environment()
    if _ENV == EnvironmentType.PRODUCTION:
        run_server()
    elif _ENV == EnvironmentType.DEVELOPMENT:
        run_server(True)
    else:
        print(f"Not found {_ENV}, process is stopped")
