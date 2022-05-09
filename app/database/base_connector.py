import mysql.connector
from mysql.connector import errorcode
from sanic.log import logger

from app.config import AppConfig


class BaseConnector:
    def __init__(self):
        self._connection = None

    def connect(self):
        try:
            _host = AppConfig.Global.SQL.HOST
            _port = AppConfig.Global.SQL.PORT
            _user_name = AppConfig.Global.SQL.USER_NAME
            _password = AppConfig.Global.SQL.PASSWORD
            _database = AppConfig.Global.SQL.DATABASE_NAME
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
