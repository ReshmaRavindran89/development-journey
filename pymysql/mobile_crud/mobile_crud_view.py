from mysql import connector

class MobileListRetrieveUpdateDelete:

    def __init__(self):
        
       try:

            self.connection = connector.connect(

            host = "localhost",
            user = "root",
            password = "Password@123",
            database = "mobile_db"
            )

            self.cursor = self.connection.cursor()

            print("db connection ok....")

       except Exception as e:

            print(e)

    def list(self):

           query ="select * from mobile"  

           self.cursor.execute(query) 

           records =  self.cursor.fetchall()

           if records:
                
                for row in records:

                       print(row) 

           else:
                
                print("no records found.....")


    def create(self,title=None,brand=None,specs=None,price=None):
         
      query = """

            insert into mobile (title,brand,specs,price) values (%s,%s,%s,%s)

        """ 

      data =  (title,brand,specs,price)

      self.cursor.execute(query,data)
         
      self.connection.commit()

      print("record inserted....")
         
    def retrieve(self,id=None):
         
        query = "select * from mobile where id = %s"

        data = (id,)

        self.cursor.execute(query,data)

        record = self.cursor.fetchone()

        print(record)  

    def delete(self,id=None):

        query = "delete from mobile where id = %s"

        data = (id,)

        self.cursor.execute(query,data)

        self.connection.commit()

        print("record deleted....")     

     

mobile_instance = MobileListRetrieveUpdateDelete()
#mobile_instance.create(title= "iPhone 14",brand= "Apple",specs= "128GB, 6GB RAM", price=79999)
#mobile_instance.create(title= "Galaxy S23",brand= "Samsung",specs= "256GB, 8GB RAM", price=74999)
#mobile_instance.create(title= "OnePlus 11",brand= "OnePlus",specs= "256GB, 16GB RAM", price=56999)
mobile_instance.retrieve(id=1)
mobile_instance.delete(id=1)
mobile_instance.list()




