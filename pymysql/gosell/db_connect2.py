from mysql import connector

# step1:- establish a connection

connection = connector.connect(
host = "localhost",
user = "root",
password = "Password@123",
)

cursor = connection.cursor()

query = "create database gosell_db"

cursor.execute(query)

connection.commit()

print("completed")
