


number = 12345

print(f"number: {number}")
print("Digits (from right to left):")

# number is 0

if number == 0:
    print(0)

while number > 0:

    # modulo 10 to get the last digit

    digit = number % 10
    print(digit)
    
    # floor division to remove the last digit

    number = number // 10