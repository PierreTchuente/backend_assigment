import mysql.connector

from service_api.config import Config

db_setting = Config.get_db_setting()
logger = Config.get_logger()


class MySQLDb:
    @staticmethod
    def get_connection():
        try:
            return mysql.connector.connect(**db_setting)
        except mysql.connector.Error as err:
            raise err
