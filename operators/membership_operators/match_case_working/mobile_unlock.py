"""
 Mobile Unlock System
------------------------------------
Task:
- Ask for unlock pattern

If pattern is correct:
    - Ask for fingerprint
    - If fingerprint matches:
        "Phone unlocked"
    - Else:
        "Fingerprint mismatch"
Else:
    "Wrong pattern"

"""
pattern = input("Enter pattern: ")

if pattern == "1234":
    print("Wrong pattern")
else:
    fingerprint = input("Scan fingerprint: ")
    if fingerprint == "match":
        print("Phone unlocked")
    else:
        print("Fingerprint mismatch")