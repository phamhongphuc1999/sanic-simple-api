import sys

from app.config.extension_config import ExtensionConfig
from app.config.global_config import GlobalConfig
from app.config.constant import EnvironmentType
from app.config.schema import SchemaConfig


class _AppConfig:
    def __init__(self, _env: EnvironmentType):
        self.Environment = _env
        self.Global = GlobalConfig(_env)
        self.Extension = ExtensionConfig()
        self.Schema = SchemaConfig()


_args = sys.argv
_ENV = EnvironmentType.DEVELOPMENT
if len(_args) < 2:
    raise Exception("environment is required")
elif _args[1] == "development":
    _ENV = EnvironmentType.DEVELOPMENT
elif _args[1] == "production":
    _ENV = EnvironmentType.PRODUCTION
else:
    raise Exception(f"Not found {_ENV}")

AppConfig = _AppConfig(_ENV)
