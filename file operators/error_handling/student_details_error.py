"""
Create a program that:
Takes student name
Takes course fee
Takes amount paid
Raise error if:
Fee is negative
Paid amount is negative
Paid amount is greater than fee
Handle invalid input
Always print "Registration Process Finished" using finally

"""
try:

# student name :-

    student_name = input("enter name: ")

# course fee :-

    course_fee = int(input("enter course fee: "))

# amount paid :-

    total_amount_paid = int(input("enter total amount paid: "))

# raise error :- 
if course_fee<0:
        
    raise Exception("Fee is negative") 

if total_amount_paid<0:

     raise Exception("Paid amount is negative") 

if total_amount_paid > course_fee:

    raise Exception("Paid amount is greater than fee")

else:

    raise Exception(" ")
