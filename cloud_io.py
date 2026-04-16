import pandas as pd
import mysql.connector
from mysql.connector import Error
import os, sys
from constants import *
from exception import CustomException


class MySQLIO:
    connection = None

    def __init__(self):
        if MySQLIO.connection is None or not MySQLIO.connection.is_connected():
            # Try to get credentials from Streamlit secrets first (for cloud deployment)
            try:
                import streamlit as st
                host = st.secrets["mysql"]["host"]
                user = st.secrets["mysql"]["user"]
                password = st.secrets["mysql"]["password"]
                database = st.secrets["mysql"]["database"]
            except:
                # Fallback to environment variables (for local development)
                host = os.getenv(MYSQL_HOST_KEY, "localhost")
                user = os.getenv(MYSQL_USER_KEY, "root")
                password = os.getenv(MYSQL_PASSWORD_KEY, "")
                database = os.getenv(MYSQL_DATABASE_KEY, MYSQL_DATABASE_NAME)

            try:
                self._ensure_database_exists(host, user, password, database)
                MySQLIO.connection = mysql.connector.connect(
                    host=host,
                    user=user,
                    password=password,
                    database=database
                )
            except Error as e:
                raise Exception(f"MySQL connection failed: {e}")

        self.connection = MySQLIO.connection

    def _ensure_database_exists(self, host, user, password, database):
        try:
            temp_conn = mysql.connector.connect(host=host, user=user, password=password)
            cursor = temp_conn.cursor()
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS `{database}`")
            temp_conn.commit()
            cursor.close()
            temp_conn.close()
        except Error as e:
            raise Exception(f"Failed to ensure database exists: {e}")

    def _sanitize_table_name(self, name: str) -> str:
        return name.replace(" ", "_").replace("-", "_").lower()

    def _create_table_if_not_exists(self, table_name: str):
        cursor = self.connection.cursor()
        cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS `{table_name}` (
                id INT AUTO_INCREMENT PRIMARY KEY,
                product_name VARCHAR(500),
                over_all_rating VARCHAR(50),
                price VARCHAR(100),
                date VARCHAR(100),
                rating VARCHAR(50),
                name VARCHAR(255),
                comment TEXT
            )
        """)
        self.connection.commit()
        cursor.close()

    def store_reviews(self, product_name: str, reviews: pd.DataFrame):
        try:
            table_name = self._sanitize_table_name(product_name)
            self._create_table_if_not_exists(table_name)

            cursor = self.connection.cursor()
            insert_query = f"""
                INSERT INTO `{table_name}`
                (product_name, over_all_rating, price, date, rating, name, comment)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            rows = [
                (
                    str(row.get("Product Name", "")),
                    str(row.get("Over_All_Rating", "")),
                    str(row.get("Price", "")),
                    str(row.get("Date", "")),
                    str(row.get("Rating", "")),
                    str(row.get("Name", "")),
                    str(row.get("Comment", "")),
                )
                for _, row in reviews.iterrows()
            ]
            cursor.executemany(insert_query, rows)
            self.connection.commit()
            cursor.close()

        except Exception as e:
            raise CustomException(e, sys)

    def get_reviews(self, product_name: str) -> pd.DataFrame:
        try:
            table_name = self._sanitize_table_name(product_name)
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute(f"SELECT * FROM `{table_name}`")
            rows = cursor.fetchall()
            cursor.close()

            if not rows:
                return pd.DataFrame()

            df = pd.DataFrame(rows)
            df.rename(columns={
                "product_name": "Product Name",
                "over_all_rating": "Over_All_Rating",
                "price": "Price",
                "date": "Date",
                "rating": "Rating",
                "name": "Name",
                "comment": "Comment",
            }, inplace=True)

            if "id" in df.columns:
                df.drop(columns=["id"], inplace=True)

            return df

        except Exception as e:
            raise CustomException(e, sys)

    def list_product_tables(self) -> list:
        try:
            cursor = self.connection.cursor()
            cursor.execute("SHOW TABLES")
            tables = [row[0] for row in cursor.fetchall()]
            cursor.close()
            return tables
        except Exception as e:
            raise CustomException(e, sys)
