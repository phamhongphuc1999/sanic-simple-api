from sanic import json, Blueprint

user_blueprint = Blueprint("user_blueprint")


@user_blueprint.get("/register")
async def register_user(request):
    try:
        return json({'hello': 'world'})
    except Exception as error:
        return json({"error": error}, status=400)
