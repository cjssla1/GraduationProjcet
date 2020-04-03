import MySQLdb

conn = MySQLdb.connect(host='10.100.100.4', port=3306, user='dbid', passwd='pw', db='dbname', charset='utf8')
#import mysql.connector
#conn = mysql.connector.connect(host='10.100.100.4', port='3306', user='dbid', password='pw', database='dbname', charset='utf8')



curs = conn.cursor()


sql = "select * from table_A"
curs.execute(sql)

data = curs.fetchall()
data[0] #첫번째 row
data[1] #두번째 row


conn.close()
