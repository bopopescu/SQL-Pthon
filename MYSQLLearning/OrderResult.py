import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="68221102a",
    database="testDb"
)

mycursor = db.cursor()
#ORDER BY will sort the list by what you specify default is ascending order
sql = "SELECT * FROM teachers ORDER BY age DESC"
mycursor.execute(sql)
myresult = mycursor.fetchall()

for i in myresult:
    print(i)
