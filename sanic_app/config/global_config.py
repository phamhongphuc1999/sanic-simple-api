class _AppConfig:
    APP_NAME = "sanic_simple_api"


class _GlobalConfig:
    def __init__(self):
        self.AppConfig = _AppConfig
