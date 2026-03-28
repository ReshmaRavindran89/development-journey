from mysql import connector

# step 1:- establish a connection connector > connect()

connection = connector.connect(
host = "localhost",
user = "root",
password = "Password@123"
)
print(connection)

# step 2: to execute query

cursor = connection.cursor()

query = "create database py_db"

cursor.execute(query)

connection.commit() 

print("completed")
