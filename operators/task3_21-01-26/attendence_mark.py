# Read two values attendance and mark and print the result of attendance >= 75 and mark >= 40

attendence =int(input("Enter the Attendence: "))
mark =int(input("Enter the Marks: "))
result = attendence>=75 and mark>=40
print("Result of Attendence: ",result)
