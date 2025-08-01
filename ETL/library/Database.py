import mysql.connector
from .Variables import Variables
from .Logger import Logger
from mysql.connector import Error


class Database():
    def __init__(self, logger: Logger):
        try:
            self.logger = logger
            self.conn = mysql.connector.connect(
                host=Variables.get_variable('DB_HOST'),
                user=Variables.get_variable('DB_USER'),
                password=Variables.get_variable('DB_PASSWORD'),
                database=Variables.get_variable('DB_STG'),
                allow_local_infile=True
            )
            self.cursor = self.conn.cursor()
        except Error as e:
            self.logger.log_error('Error connecting to Database: {e}')
            self.conn = None
            self.cursor = None

    def connect(self):
        pass

    def execute_query(self, query):
        try:
            self.logger.log_info(query)
            if not self.conn or not self.cursor:
                self.logger.log_error("No active database connection.")
                return None
            self.cursor.execute(query)
            if query.strip().upper().startswith("SELECT"):
                return self.cursor.fetchall()
            else:
                self.conn.commit()
                self.logger.log_info("Query executed successfully.")
        except Error as e:
            self.logger.log_error(f"Error executing query: {e}")
            return None

    def disconnect(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
            self.logger.log_info("Database connection closed.")
