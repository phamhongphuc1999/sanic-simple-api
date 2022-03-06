from sanic import json, Blueprint
import json as json_format

from sanic_app.factory.database import database_factory

employee_blueprint = Blueprint("user_blueprint")


@employee_blueprint.post("/register")
async def register_user(request):
    try:
        return json({'hello': 'world'})
    except Exception as error:
        return json({"error": error}, status=400)


@employee_blueprint.post("/login")
async def login_app(request):
    try:
        employee_data = json_format.loads(request.body)
        username = employee_data["username"]
        password = employee_data["password"]
        user_data = database_factory.get_query().user_query().get_employee_by_username_password(username, password)
        return json(user_data)
    except Exception as error:
        return json({"error": error}, status=400)
