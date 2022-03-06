import mysql.connector
from mysql.connector import errorcode
from sanic.log import logger

from sanic_app.config import GlobalAppConfig


class BaseConnector:
    def __init__(self):
        self._connection = None

    def connect(self):
        try:
            _host = GlobalAppConfig.MySQLConfig.HOST
            _port = GlobalAppConfig.MySQLConfig.PORT
            _user_name = GlobalAppConfig.MySQLConfig.USER_NAME
            _password = GlobalAppConfig.MySQLConfig.PASSWORD
            _database = GlobalAppConfig.MySQLConfig.DATABASE_NAME
            self._connection = mysql.connector.connect(host=_host, user=_user_name, password=_password,
                                                       database=_database)
            logger.info(f"Connected - host: {_host}, port: {_port}")
            return self._connection
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                logger.error("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                logger.error("Database does not exist")
            else:
                logger.error(err)
            return None

    def get_connection(self):
        return self._connection

    def get_cursor(self):
        return self._connection.cursor()

    def close_connection(self):
        self._connection.close()
