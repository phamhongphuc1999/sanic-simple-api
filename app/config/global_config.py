from app.config.constant import EnvironmentType


class GlobalConfig:
    def __init__(self, _env: EnvironmentType):
        self.App = self._App(_env)
        self.SQL = self._SQL(_env)

    class _App:
        def __init__(self, _env: EnvironmentType):
            self.NAME = "sanic_simple_api"
            self.PORT = 3000
            self.HOST = '0.0.0.0'

    class _SQL:
        def __init__(self, _env: EnvironmentType):
            self.PORT = 3306
            self.USER_NAME = "root"
            self.PASSWORD = "sanic"
            self.DATABASE_NAME = "sanic_app"
            if _env == EnvironmentType.DEVELOPMENT:
                self.HOST = "127.0.0.1"
            elif _env == EnvironmentType.DEV_DOCKER:
                self.HOST = "docker.for.mac.host.internal"
            else:
                raise Exception(f"Not found {_env} environment config")
