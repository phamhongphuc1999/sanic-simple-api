from sanic_app.config.utils import EnvironmentType


class _DevAppConfig:
    APP_NAME = "sanic_simple_api"
    APP_PORT = 8000
    APP_HOST = '0.0.0.0'


class _ProAppConfig:
    APP_NAME = "sanic_simple_api"
    APP_PORT = 8000
    APP_HOST = '0.0.0.0'


class _DevMySQLConfig:
    HOST = "127.0.0.1"
    PORT = 3306
    USER_NAME = "root"
    PASSWORD = "sanic"
    DATABASE_NAME = "sanic_app"


class _ProMySQLConfig:
    HOST = "127.0.0.1"
    PORT = 3306
    USER_NAME = "root"
    PASSWORD = "sanic"
    DATABASE_NAME = "sanic_app"


class _GlobalConfig:
    def __init__(self, _env: EnvironmentType):
        if _env == "development":
            self.AppConfig = _DevAppConfig
            self.MySQLConfig = _DevMySQLConfig
        elif _env == "production":
            self.AppConfig = _ProAppConfig
            self.MySQLConfig = _ProMySQLConfig
