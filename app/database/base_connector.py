from typing import Union

import mysql.connector
from mysql.connector import errorcode, CMySQLConnection, MySQLConnection
from mysql.connector.cursor import MySQLCursor

from app.config import AppConfig
from app.services.logger_service import app_logger


class BaseConnector:
    def __init__(self):
        self._connection: Union[CMySQLConnection, MySQLConnection]
        self._connect()

    def _connect(self):
        try:
            _host = AppConfig.Global.SQL.HOST
            _port = AppConfig.Global.SQL.PORT
            _user_name = AppConfig.Global.SQL.USER_NAME
            _password = AppConfig.Global.SQL.PASSWORD
            _database = AppConfig.Global.SQL.DATABASE_NAME
            self._connection = mysql.connector.connect(host=_host, user=_user_name, password=_password,
                                                       database=_database)
            app_logger.info(f"Connected - host: {_host}, port: {_port}")
            return self._connection
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                app_logger.error("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                app_logger.error("Database does not exist")
            else:
                app_logger.error(err)
            return None

    def get_connection(self) -> Union[CMySQLConnection, MySQLConnection]:
        return self._connection

    def get_cursor(self) -> MySQLCursor:
        return self._connection.cursor()

    def close_connection(self):
        self._connection.close()
