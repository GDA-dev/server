import pymysql.cursors
from dotenv import dotenv_values

pymysql.version_info = (1, 4, 3, "final", 0)
pymysql.install_as_MySQLdb()

env = dotenv_values(".env")

connection = pymysql.connect(
    password=env["PASSWORD"], 
    user=env["USER"], 
    host=env["HOST"], 
    port=int(env["PORT"]), 
    db=env["NAME"], 
    ssl_verify_cert=env['MYSQL_ATTR_SSL_CA'], 
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

db = connection.cursor()