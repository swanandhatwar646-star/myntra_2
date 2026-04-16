from src.cloud_io import MySQLIO
from src.exception import CustomException
import os, sys


def fetch_product_names_from_cloud():
    try:
        mysql_io = MySQLIO()
        tables = mysql_io.list_product_tables()
        return [table.replace("_", " ") for table in tables]

    except Exception as e:
        raise CustomException(e, sys)
