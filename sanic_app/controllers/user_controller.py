from sanic import Blueprint, json

from sanic_app.sanic_app import main_app


class UserController:
    def __init__(self, user_blueprint: Blueprint):
        self._user_blueprint = user_blueprint

    @main_app.get("/register")
    async def register_user(self, request):
        try:
            return json({'hello': 'world'})
        except Exception as error:
            return json({"error": error})
