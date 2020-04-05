#!usr/bin/python3

db = MySQLdb.connect("localhost","admin","1234","stock")

cursor = db.cursor()

cursor.execute("SELECT VERSION()")

data = cursor.fetchone()

print("Database version : {}".format(data))


sql = "select * from table_A"
cursor.execute(sql)

data = cursor.fetchall()
#data[0] #첫번째 row
#data[1] #두번째 row


conn.close()
