"""
import mysql.connector

 

connection = mysql.connector.connect(user = "root", database = "quickbanking", password = "Hikmet1q.")

 

cursor = connection.cursor()

 

testQuery = ("SELECT * FROM account")

 

cursor.execute(testQuery)

 

for item in cursor:

    print(item)

 

cursor.close()

connection.close()
"""