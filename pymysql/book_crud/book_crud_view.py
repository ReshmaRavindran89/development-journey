from mysql import connector

class BookListRetrieveUpdateDelete:

    def __init__(self):

        try:
        
            self.connection = connector.connect(

            host = "localhost",
            user = "root",
            password = "Password@123",
            database = "book_db"
            )


            self.cursor = self.connection.cursor()

            print("db connection ok....")

        except Exception as e:

            print(e)

    def list(self):

        query = "select * from book "

        self.cursor.execute(query)

        records = self.cursor.fetchall()

        if records:

            for row in records:

                print(row)

        else:

            print("no records found...")

    def create(self,title=None,author=None,price=None,publisher=None,genre=None,year=None):

        query = """
        
                insert into book (title,author,price,publisher,genre,year) values (%s,%s,%s,%s,%s,%s)
            
            """

        data = (title,author,price,publisher,genre,year)

        self.cursor.execute(query,data)

        self.connection.commit()

        print("record inserted....")

    def retrieve(self,id=None):

        query = "select * from book where id = %s"

        data = (id,)

        self.cursor.execute(query,data)

        record = self.cursor.fetchone()

        print(record)

    def delete(self,id=None):

        query = "delete from book where id = %s"

        data = (id,)

        self.cursor.execute(query,data)

        self.connection.commit()

        print("record deleted....")

    def update(self,id=None,**kwargs):

        place_holder = ""

        for k in kwargs.keys():

            place_holder += f"{k}=%s,"

        place_holder=place_holder.rstrip(",")

        query = f"update book set {place_holder} where id= {id}"

        data = [v for v in kwargs.values()]

        self.cursor.execute(query,data)

        self.connection.commit()

        print("record updated......")

book_instance = BookListRetrieveUpdateDelete()
#book_instance.create(title="randamoozham",author="ST",price=580,publisher="HYT",genre="fiction",year=1984)
#book_instance.create(title="RAM C/O ANANDHI",author="Akhil P Dharmajan",price=300,publisher="DC Books",genre="fiction",year=2020)
#book_instance.retrieve(id=1)
#book_instance.delete(id=1)
book_instance.update(id=2,title="Randammoozham",price=650,year=2000)
book_instance.list()
book_instance.retrieve(id=2)
