import os
import mysql.connector
from mysql.connector import Error

def get_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )


def initialize_database():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""

        CREATE TABLE IF NOT EXISTS students(

            id INT AUTO_INCREMENT PRIMARY KEY,

            name VARCHAR(100),

            email VARCHAR(100),

            course VARCHAR(100)

        )

    """)

    conn.commit()

    cursor.close()

    conn.close()