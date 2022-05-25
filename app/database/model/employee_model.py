import mysql.connector
from sanic.log import logger

from app.database.base_connector import BaseConnector


class _EmployeeModel:
    _GET_USER_SCRIPT = "SELECT * FROM Employees WHERE username = '{username}' AND password = '{password}';"

    def __init__(self, connection: BaseConnector):
        self._connection = connection

    def get_employee_by_username_password(self, username: str, password: str):
        try:
            _cursor = self._connection.get_cursor()
            employee_data = _cursor.execute("SELECT * FROM Employees;")
            print("employee_data", employee_data)
            return employee_data
        except mysql.connector.Error as error:
            logger.error(str(error))
        except Exception as error:
            logger.error(str(error))
        return None
