#WAP to calculate gross salary from basic salary

Basic_salary =float(input("Enter the Basic salary:"))

HR = Basic_salary * 30 / 100
TA = Basic_salary *40 / 100
DA = Basic_salary * 20 / 100

Gross_salary = Basic_salary + HR + TA + DA

print("House Range of 30 % of Basic_salary:", HR)
print("Travelling Allowance of 40 % of Basic_salary:", TA)
print("Daily Allowance of 20 % of Basic_salary:",DA)
print("Gross salary:",Gross_salary)