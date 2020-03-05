import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="68221102a",
    database="testDb"
)

mycursor = db.cursor()
mycursor.execute("SELECT * FROM teachers")
# this will create a list of all thge rows selected from the last  mycursor.execute
myResults = mycursor.fetchall()
print(myResults)
# to iterate through the list for individual rows
for i in myResults:
    print(i)
mycursor.execute("SELECT age FROM teachers")
myResults1 = mycursor.fetchall()
for i in myResults1:
    print(i)
# this fetches on reslut instead of full list
mycursor.execute("SELECT * FROM teachers")
myResults1 = mycursor.fetchone()
for i in myResults1:
    print(i)
