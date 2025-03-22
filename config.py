import mysql.connector
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

db_config = {
    "host": "127.0.0.1",  # Use explicit IP instead of "localhost"
    "port": 3306,  # MySQL default port
    "user": "root",  # Change if using a different user
    "password": "pradnya1512",
    "database": "secure_user_auth",
    "use_pure": True ,
}


def get_db_connection():
    return mysql.connector.connect(**db_config)
