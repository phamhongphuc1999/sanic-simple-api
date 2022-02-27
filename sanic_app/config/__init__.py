from sanic_app.config.global_config import _GlobalConfig
from sanic_app.config.utils import EnvironmentType
from sanic_app.services.utils import get_environment

GlobalAppConfig = _GlobalConfig(get_environment())
