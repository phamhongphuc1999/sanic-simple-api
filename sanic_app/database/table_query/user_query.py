from mysql.connector import CMySQLConnection
from sanic.log import logger


class _UserQuery:
    _GET_USER_SCRIPT = "SELECT * FROM user WHERE user_name = %s AND password = %s"

    def __init__(self, cursor: CMySQLConnection):
        self._cursor = cursor

    def get_user_by_username_password(self, username: str, password: str):
        try:
            user_data = self._cursor.execute(_UserQuery._GET_USER_SCRIPT, (username, password))
            return user_data
        except Exception as error:
            logger.error(str(error))
            return None
