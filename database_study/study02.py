import mysql.connector

cnx = mysql.connector.connect(user="root", password="mirim", host="127.0.0.1", port="3307", database="mydatabase" )

cursor = cnx.cursor()
#cursor객체를 가져오면 query문을 실행할 수 있음

cursor.execute("DROP TABLE IF EXISTS person")

ddl = """
CREATE TABLE IF NOT EXISTS person(
    id int(11) NOT NULL AUTO_INCREMENT,
    name varchar(255) NOT NULL,
    age int(11) NOT NULL,
    birthday timestamp NOT NULL,
    PRIMARY KEY(id)
) ENGINE = InnoDB
"""

cursor.execute(ddl)

cursor.execute("""
CREATE TABLE IF NOT EXISTS blob_text (
    id int(11) NOT NULL AUTO_INCREMENT,
    data BLOB NOT NULL,
    PRIMARY KEY(id)
    ) ENGINE=InnoDB
""")

cursor.close()
cnx.close()