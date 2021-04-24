import mysql.connector

cnx = mysql.connector.connect(user="root", password="mirim", host="127.0.0.1", port="3307", database="mydatabase" )

cursor = cnx.cursor()

truncate_query = "TRUNCATE TABLE blob_test"
cursor.execute(truncate_query)

# f = open("python-logo.png", 'rb')
with open("python-logo.png", 'rb') as f:
    binary = f.read()
    insert_blob_query = "INSERT INTO blob_test (data) VALUES (%s)"
    #BLOB 데이터 저장 (bytes 타입 저장)
    cursor.execute(insert_blob_query, (binary,))
    cnx.commit()

cnx.close()