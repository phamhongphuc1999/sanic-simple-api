from sanic.log import logger


class _EmployeeModel:
    _GET_USER_SCRIPT = "SELECT * FROM employees WHERE username=%s AND password=%s"

    def __init__(self, connection):
        self._connection = connection

    def get_employee_by_username_password(self, username: str, password: str):
        try:
            _cursor = self._connection.cursor()
            employee_data = _cursor.execute(_EmployeeModel._GET_USER_SCRIPT, (username, password))
            _cursor.close()
            print(employee_data)
            return employee_data
        except Exception as error:
            logger.error(str(error))
            return None
