import pymysql.cursors
import os
from dotenv import load_dotenv
load_dotenv()


connection = pymysql.connect(
    password=os.getenv("PASSWORD"),
    user=os.getenv("USER"),
    host=os.getenv("HOST"),
    port=int(os.getenv("PORT")),
    db=os.getenv("NAME"),
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

db = connection.cursor()