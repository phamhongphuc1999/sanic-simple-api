from sanic_app.database.table_query.employee_query import _EmployeeQuery


class TableQuery:
    def __init__(self, connection):
        self._user = _EmployeeQuery(connection)

    def user_query(self):
        return self._user
