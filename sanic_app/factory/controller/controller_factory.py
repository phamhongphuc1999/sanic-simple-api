from sanic_app.config.utils import ServiceType
from sanic_app.controllers.user_controller import UserController


class ControllerFactory:
    def __init__(self):
        self._user_controller = None

    def create_controller(self, _type: ServiceType):
        if _type == ServiceType.USER:
            if self._user_controller is None:
                self._user_controller = UserController()
