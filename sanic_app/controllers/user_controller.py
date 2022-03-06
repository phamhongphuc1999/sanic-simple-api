from sanic import json, Blueprint
import json as json_format

user_blueprint = Blueprint("user_blueprint")


@user_blueprint.post("/register")
async def register_user(request):
    try:
        return json({'hello': 'world'})
    except Exception as error:
        return json({"error": error}, status=400)


@user_blueprint.post("/login")
async def login_app(request):
    try:
        user_data = json_format.loads(request.body)
        username = user_data["username"]
        password = user_data["password"]
        print(f"{username}{password}")
        return json(user_data)
    except Exception as error:
        return json({"error": error}, status=400)
