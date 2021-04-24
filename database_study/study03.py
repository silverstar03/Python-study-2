import datetime

import mysql.connector

cnx = mysql.connector.connect(user="root", password="mirim", host="127.0.0.1", port="3307", database="mydatabase" )

cursor = cnx.cursor()

truncate_query = "TRUNCATE TABLE person"
cursor.execute(truncate_query)

insert_query = "INSERT INTO person (name, age, birthday) VALUES(%s, %s, %s)"
cursor.execute(insert_query, ("김철수", 20, datetime.date(1990, 10, 1)))
rowid = cursor.lastrowid
print(f"cursor.rowid :  {rowid}")
cnx.commit()

records = [("이영희", 30, datetime.date(1980, 10, 1)), ("박미림", 40, datetime.date(1970, 10, 1))]
cursor.executemany(insert_query, records)
print(f"cursor.rowcount : {cursor.rowcount}")
cnx.commit()

# cursor.execute("SELECT * FROM person")
cursor.execute("SELECT * FROM person WHERE id <= %s", (10,))
#한 개의 튜플은 ','을 사용하여 튜플임을 알려줘야 함.
rows = cursor.fetchall() #이전에 select를 한 후에 호출해줘야 함.
for rid, name, age, birthday in rows:
    print("row", rid, name, age, birthday)

cnx.close()