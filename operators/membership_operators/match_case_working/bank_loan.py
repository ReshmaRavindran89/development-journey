"""
Bank Loan Eligibility
------------------------------------
Task:
- Ask for monthly income

If income ≥ 25,000:
    - Ask for credit score
    - If credit score ≥ 700:
        "Loan approved"
    - Else:
        "Low credit score"
Else:
    "Income not sufficient"
"""
income = int(input("Monthly income: "))

if income < 25000:
    print("Income not sufficient")
else:
    credit_score = int(input("Credit score: "))
    if credit_score < 700:
        print("Low credit score")
    else:
        print("Loan approved")