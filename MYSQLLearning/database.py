#!/usr/bin/python3
#this teaches how to create a database and how to create a table

import pymysql

# Open database connection
mydb = pymysql.connect(host = "localhost",
                     user = "Nyiko",
                     password = "1234",
                     )

# a cursor is used to communicate with the the database after establishing connection
myCursor =  mydb.cursor()
#The my cursor has a command caled executwe which runs SQL Language]
#When running this a second time i had to comment out line below as table would have aready been made
#myCursor.execute("CREATE DATABASE testDb")

#this creates a list of databases
myCursor.execute("SHOW DATABASES")
#We the iterate through the database list made for cursor to print each database
for db in myCursor:
    print(db)






# prepare a cursor object using cursor() method
#cursor = db.cursor()
#https://www.youtube.com/watch?v=-YU36D7oTLA&list=PLB5jA40tNf3tRMbTpBA0N7lfDZNLZAa9G&index=2
#https://www.youtube.com/watch?v=tGinfzlp0fE
#
# execute SQL query using execute() method.
#cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
#data = cursor.fetchone()
#print ("Database version : %s " % data)

# disconnect from server
#db.close()
print(mydb)

