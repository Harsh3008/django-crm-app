import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'harsh123'
)
#Prepare a curson object
cursorObject = dataBase.cursor()

# Create a database

cursorObject.execute("CREATE DATABASE harshdb")

print("All Done")