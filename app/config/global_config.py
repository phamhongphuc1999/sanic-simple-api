from app.config.constant import EnvironmentType


class GlobalConfig:
    def __init__(self, _env: EnvironmentType):
        self.App = self._App(_env)
        self.SQL = self._SQL(_env)

    class _App:
        def __init__(self, _env: EnvironmentType):
            self.NAME = "sanic_simple_api"
            self.PORT = 8000
            self.HOST = '0.0.0.0'

    class _SQL:
        def __init__(self, _env: EnvironmentType):
            self.HOST = "127.0.0.1"
            self.PORT = 3306
            self.USER_NAME = "root"
            self.PASSWORD = "sanic"
            self.DATABASE_NAME = "sanic_app"
