import mysql.connector

cnx = mysql.connector.connect(user="root", password="mirim", host="127.0.0.1", port="3307", database="mydatabase" )

cursor = cnx.cursor()
cursor.execute("SELECT name, age FROM person LIMIT 1 OFFSET 0")
#offset은 시작위치를 가리킴 limit은 가져올 개수
row = cursor.fetchone()

print(row)
print(type(row))
print(row[0], row[1])
cursor.close()


cursor = cnx.cursor(dictionary=True)
cursor.execute("SELECT name, age FROM person LIMIT 1 OFFSET 0")
row = cursor.fetchone()

print(row)
print(type(row))
print(row['name'], row['age'])

cnx.close()