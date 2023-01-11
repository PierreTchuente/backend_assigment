import mysql.connector

from service_api.config import Config

# from mysql.connector import errorcode


db_setting = Config.get_db_setting()
logger = Config.get_logger()


class MySQLDb:
    @staticmethod
    def get_connection():
        try:
            return mysql.connector.connect(db_setting)
        except mysql.connector.Error as err:
            raise err
            # if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            #     self.logger.exception("Something is wrong with
            #     your user name or password")
            # elif err.errno == errorcode.ER_BAD_DB_ERROR:
            #     self.logger.exception("Database does not exist")
            # else:
            #     self.logger.exception(err)
