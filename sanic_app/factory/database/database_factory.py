from sanic_app.database.base_connector import BaseConnector
from sanic_app.database.table_query import TableQuery


class DatabaseFactory:
    def __init__(self):
        self._base_query = None

    def get_query(self):
        if self._base_query is None:
            _base_connector = BaseConnector()
            self._base_query = TableQuery(_base_connector.get_cursor())
        return self._base_query
