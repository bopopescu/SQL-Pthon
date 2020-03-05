import mysql.connector

# this is how we connect to the databvase
dbs = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="68221102a",
    database="testDb"
)
# this print how the object of the database connection is made
print(dbs)
print("im dumb")
mycursor = dbs.cursor()
# How to create tables
mycursor.execute("CREATE TABLE teachers( name VARCHAR(20) , age INT )  ")

mycursor.execute("SHOW TABLES")
for table in mycursor:
    print(table)

# db = mysql.connector.connect(host = "localhost",
#  user = "root",
# passwrd = "68221102a",

# )

# print(dbs)
