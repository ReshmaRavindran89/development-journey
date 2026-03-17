"""
4. Movie Ticket Booking
------------------------------------
Task:
- Ask for age

If age ≥ 18:
    - Ask for seat availability
    - If seats available:
        "Ticket booked"
    - Else:
        "House full"
Else:
    "Not eligible to watch the movie"
"""

available_seat = 8
age = int(input("Enter your age: "))

if age >= 18:

    if available_seat > 0:
        print("Ticket booked")
    else:
        print("House full")
else:
    print("Not eligible to watch the movie")