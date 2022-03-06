from mysql.connector import CMySQLConnection

from sanic_app.database.table_query.user_query import _UserQuery


class TableQuery:
    def __init__(self, cursor: CMySQLConnection):
        self._user = _UserQuery(cursor)

    def user_query(self):
        return self._user
