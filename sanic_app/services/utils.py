import sys

from sanic_app.config import EnvironmentType


def get_environment():
    _args = sys.argv
    if len(_args) > 1:
        _env = _args[1]
        if _env == "development":
            return EnvironmentType.DEVELOPMENT
        elif _env == "production":
            return EnvironmentType.PRODUCTION
        else:
            raise Exception(f"Not found {_env}")
