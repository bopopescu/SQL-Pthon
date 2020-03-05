import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="68221102a",
    database="testDb"
)

mycursor = db.cursor()
# sql statement to do retieveing
sql = "SELECT * FROM teachers WHERE name = 'A'"
# execute querie
mycursor.execute(sql)
# put the results of the querie in a list
myesult = mycursor.fetchall()
# iterate
for result in myesult:
    print(result)

    # Wildcard include the start of ,end of and conatin if searching
    # WIldcrards '%as%' means conatin as in the word , MI% means at the beginning
    # %ke

sql1 = "SELECT * FROM teachers WHERE name LIKE '%ac%'"
mycursor.execute(sql1)
myresult = mycursor.fetchall()

for result in myresult:
    print(result)
# this is safer for sql injections as it prepares the statements with a placeholder
sql2 = "SELECT * FROM teachers WHERE name LIKE %s"
placeholder = '%hn%',  # when dealing with one value you must include the comma afterawrds
mycursor.execute(sql2, placeholder)
myresult = mycursor.fetchall()

for result in myresult:
    print(result)
