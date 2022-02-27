from sanic_app.database.base_connector import BaseConnector


class DatabaseFactory:
    def __init__(self):
        self._base_connector = None

    def get_connector(self):
        if self._base_connector is None:
            self._base_connector = BaseConnector()
        return self._base_connector
