import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="68221102a",
    database="testDb"
)
# mycusor = the conncetion made above .cursor
mycursor = db.cursor()
# You prepare the statement here for reuseablity and the %s means placeholder for a tuple
sqlFormula = "INSERT into teachers(name,age) VALUES(%s,%s)"
student1 = ("Rachel", 22)

mycursor.execute(sqlFormula, student1)
mycursor.execute("INSERT into teachers VALUES('Johnny',26)")

# we are going to insert information from a list /array
students = [("A", 22), ("B", 22), ("C", 22), ("D", 22), ("E", 22), ("F", 22), ("G", 22), ("H", 22), ("I", 22),
            ("J", 22), ("K", 22)]
# this way  is the longer version
for i in students:
    print(i)
    mycursor.execute(sqlFormula, i)

mycursor.executemany(sqlFormula, students)
# in order for change to be submitted you must use the commit function in the db
db.commit()
