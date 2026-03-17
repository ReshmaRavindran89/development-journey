# Read three marks m1,m2,m3 each out of 50
# find total
# Display A if total>140
# Display B if total in range of 130 - 140
#  Display C if total in range of 120 - 130
#  Display Fail anything below 120

m1 = int(input("Enter mark1: "))
m2 = int(input("Enter mark2: "))
m3 = int(input("Enter mark3: "))
grace_mark = 2
total = m1 + m2 + m3
if total>140:
    print("A")
elif total>=130 and total<140:
    print("B")
elif total>=120 and total<130:
    print("C")
else:
    print("FAIL")
