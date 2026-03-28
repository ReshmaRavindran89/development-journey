from mysql import connector

connection = connector.connect(
host = "localhost",
user = "root",
password = "Password@123",
database = "py_db"
)

cursor = connection.cursor()

query = """

insert into sports(name,players_count,country) values(%s,%s,%s)

"""

data = ("football","11","india")

cursor.execute(query,data)

connection.commit()

cursor.close()

connection.close()

print("data inserted.....")