from sanic import json

from sanic_app.sanic_app import user_blueprint


class UserController:
    def __init__(self):
        pass

    @user_blueprint.get("/register")
    async def register_user(self):
        try:
            return json({'hello': 'world'})
        except Exception as error:
            return json({"error": error})
