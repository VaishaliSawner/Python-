from mysql.connector import pooling
from dotenv import load_dotenv
import os
load_dotenv()


pool = pooling.MySQLConnectionPool(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_pass"),
    database=os.getenv("DB_name"),
    port=os.getenv("DB_port"),
    pool_size=10
)