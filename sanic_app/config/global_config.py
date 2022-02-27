from sanic_app.config.utils import EnvironmentType


class _DevAppConfig:
    APP_NAME = "sanic_simple_api"
    APP_PORT = 8000
    APP_HOST = '0.0.0.0'


class _ProAppConfig:
    APP_NAME = "sanic_simple_api"
    APP_PORT = 8000
    APP_HOST = '0.0.0.0'


class _GlobalConfig:
    def __init__(self, _env: EnvironmentType):
        if _env == "development":
            self.AppConfig = _DevAppConfig
        elif _env == "production":
            self.AppConfig = _ProAppConfig
