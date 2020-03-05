import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="68221102a",
    database="testDb"
)

mycursor = db.cursor()
#this is how to update
sql = "UPDATE teachers SET age = 13 WHERE name = 'A' "
mycursor.execute(sql)
#when values change in the database you must commit
db.commit()
 #this will fetch the first 5 names in database
#OFFSET is number of names to skip in the querie start from third row as OFFSET 2
mycursor.execute("SELECT * FROM teachers LIMIT 5 OFFSET 2")
myresult = mycursor.fetchall()

for i in myresult:
    print(i)


