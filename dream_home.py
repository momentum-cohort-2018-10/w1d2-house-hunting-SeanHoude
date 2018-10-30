# collect user input about income and home statistics. Include defaults and convert to usable data types

print("Welcome to the dream home down payment calculator! Please answer a few questions...")

annual_salary = input("Enter your annual salary [120000]: ") or 120000
annual_salary = int(annual_salary)
portion_saved = input("Enter the percent of your salary to save, as a decimal [0.1]: ") or .1
portion_saved = float(portion_saved)
r = input("Enter the expected annual rate of return [0.04]: ") or .04
r = float(r)
total_cost = input("Enter the cost of your dream home [1000000]: ") or 1000000
total_cost = int(total_cost)
portion_down_payment = input("Enter the percent of your home's cost to save as a down payment [0.25]: ") or .25
portion_down_payment = float(portion_down_payment)

down_payment = total_cost * portion_down_payment


# Determine number of months required to meet down payment by looping through and adding previous month's return on
# investment + monthly savings, then incrementing the number of months after each loop until savings >= down payment

def calc_months():
    months = 0
    current_savings = 0

    while current_savings <= down_payment:
        current_savings += (current_savings * r / 12) + (annual_salary / 12 * portion_saved)
        months += 1
        # print(f"Month {months}: ${int(current_savings)}")
    return months

total_months = calc_months()
print(f"Number of months: {total_months}\n")
print(f"It will take {total_months} months to save {int(down_payment)} dollars for a down payment!")


