import mysql.connector
from mysql.connector import errorcode
from sanic.log import logger

from sanic_app.config import GlobalAppConfig


class BaseConnector:
    def __init__(self):
        self._connection = None
        self._cursor = None
        self._connect()

    def _connect(self):
        try:
            _host = GlobalAppConfig.MySQLConfig.HOST
            _port = GlobalAppConfig.MySQLConfig.PORT
            _user_name = GlobalAppConfig.MySQLConfig.USER_NAME
            _password = GlobalAppConfig.MySQLConfig.PASSWORD
            _database = GlobalAppConfig.MySQLConfig.DATABASE_NAME
            self._connection = mysql.connector.connect(host=_host, user=_user_name, password=_password,
                                                       database=_database)
            self._cursor = self._connection.cursor()
            logger.info(f"Connected - host: {_host}, port: {_port}")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                logger.error("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                logger.error("Database does not exist")
            else:
                logger.error(err)

    def get_connection(self):
        return self._connection

    def get_cursor(self):
        return self._cursor

    def close_connection(self):
        self._cursor.close()
        self._connection.close()