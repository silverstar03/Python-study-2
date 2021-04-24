import mysql.connector

cnx = mysql.connector.connect(
    user="root",
    password="mirim",
    host="127.0.0.1",
    port="3307",
    database="mydatabase"
)

print(cnx.is_connected())
print(cnx.get_server_info())
print(cnx.get_server_version())

cnx.close()

print(cnx.is_connected())