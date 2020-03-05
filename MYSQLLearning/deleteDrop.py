import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="68221102a",
    database="testDb"
)

mycursor = db.cursor()
#This deletes rows meeting the condition
sql = "DELETE FROM teachers WHERE name ='A' "
mycursor.execute(sql)
db.commit()
#this deletes the whole table
sql1 = "DROP TABLE teachers "
mycursor.execute(sql1)
db.commit()
#this deletes table but will firt check its existance
sql1 = "DROP TABLE IF EXISTS teachers "
mycursor.execute(sql1)
db.commit()
#This will delete the table and remake it
sql1 = "TRUNCATE TABLE teachers "
mycursor.execute(sql1)
db.commit()




