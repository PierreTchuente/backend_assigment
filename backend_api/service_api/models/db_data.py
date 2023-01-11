# from mysql.connector import errorcode
from service_api.config import Config
from service_api.db.mysql_db import MySQLDb
from service_api.models.data import Data

logger = Config.get_logger()


class DbData:
    @staticmethod
    def create(data: Data):
        connection = MySQLDb.get_connection()
        cursor = connection.cursor()
        sql_query = f"""
            INSERT INTO data
            SET
              serial = {data.serial},
              application = {data.application},
              time = {data.time},
              type = {data.type},
              device = {data.serial},
              v0 = {data.v0},
              v1 = {data.v1},
              v2 = {data.v2},
              v3 = {data.v3},
              v4 = {data.v4},
              v5 = {data.v5},
              v6 = {data.v6},
              v7 = {data.v7},
              v8 = {data.v8},
              v9 = {data.v9},
              v10 = {data.v10},
              v11 = {data.v11},
              v12 = {data.v12},
              v13 = {data.v13},
              v14 = {data.v14},
              v15 = {data.v15},
              v16 = {data.v16},
              v17 = {data.v17}
        """

        result = cursor.execute(sql_query)
        connection.commit()
        cursor.close()
        connection.close()
        logger.info(result)
        return result

    @staticmethod
    def get(id_key: int):
        connection = MySQLDb.get_connection()
        cursor = connection.cursor()
        sql = f"""
            SELECT * FROM data
            WHERE id = {id_key}
        """
        result = cursor.execute(sql)
        logger.info(result)
        connection.close()

    @staticmethod
    def get_data(page_number: int = 1, page_size: int = 10):
        connection = MySQLDb.get_connection()
        cursor = connection.cursor()
        sql = f"""
         SELECT * FROM data
         LIMIT {page_number*page_size}, {page_size}
        """
        result = cursor.execute(sql)
        logger.info(result)
        return result
