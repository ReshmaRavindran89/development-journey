from csv import DictReader

class TransactionAnalyzer:

    def __init__(self):
       
       fr = open("bank_analyzer\\bank_transactions_500_records.csv")

       self.transcations =list(DictReader(fr))

       print(len(self.transcations),"Records found")

    def debit_transcations(self):

        for t in self.transcations: # {id:,name,type,amount}

            if t.get("type") == "debit":

                print(t)

    def credit_transcations(self):

        for t in self.transcations:

            if t.get("type") == "credit":

                print(t)

    def high_value_transcations(self):  # amount > 750000

        for t in self.transcations:

            if int(t.get("amount")) > 75000:

                print(t)

    def highest_debit_transcation(self): # amount > 50000

        for t in self.transcations:

            if t.get("type") == "debit" and int(t.get("amount")) > 50000:

                print(t)

    def highest_credit_transcation(self): # amount > 90000

        for t in self.transcations:

            if t.get("type") == "credit" and int(t.get("amount")) > 90000:

                print(t)


analysis = TransactionAnalyzer()

analysis.debit_transcations()

analysis.credit_transcations()

analysis.high_value_transcations()

analysis.highest_debit_transcation()

analysis.highest_credit_transcation()





