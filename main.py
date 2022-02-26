from sanic_app.config.extension_config import USER_ROUTER
from sanic_app.sanic_app import main_app, create_routes

if __name__ == '__main__':
    create_routes(user=USER_ROUTER)
    main_app.run()
