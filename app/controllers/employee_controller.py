from sanic import Blueprint

from app import AppConfig
from app.apis.api_response import ok_json, bad_request_json
from app.apis.api_wrapper import validate_body_with_json_schema
from app.database.model_getter import ModelGetter

employee_blueprint = Blueprint("employee_blueprint", url_prefix="/user")


@employee_blueprint.post("/register")
async def register_user(request):
    try:
        return ok_json({"hello": "123"})
    except Exception as error:
        return bad_request_json(str(error))


@employee_blueprint.post("/login")
@validate_body_with_json_schema(AppConfig.Schema.User.Login)
async def login_app(request):
    try:
        body = request.json
        username = body["username"]
        password = body["password"]
        user_data = ModelGetter.get_model().user.get_employee_by_username_password(username, password)
        return ok_json({"data": user_data})
    except Exception as error:
        return bad_request_json(str(error))
