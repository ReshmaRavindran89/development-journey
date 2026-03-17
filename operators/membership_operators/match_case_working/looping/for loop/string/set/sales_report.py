
# sales report:-
#  display day-wise sale
#  display avg sales.
#  total sales.
#  display where sales < avg sales.

sales_report = {
    "sun":23000,
    "mon":16000,
    "tue":18000,
    "wed":15000,
    "thu":19000,
    "fri":19000,
    "sat":20000,
}

for key in sales_report:
    print(key,sales_report[key])

total_sale = 0

# total sale:-

for key in sales_report:

    sale = sales_report[key]
    total_sale+=sale

print(total_sale)

# average sale:-

avg_sale = total_sale/len(sales_report)
print(avg_sale)

# Day with low sale:-

for key in sales_report:

    sale = sales_report[key]

    if sale <avg_sale:

        print("Day with Low Sale ",key,sale)


