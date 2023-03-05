name = input("enter employees name")
salary = input("enter employees salary")


if int(salary) >=2000:
    tax = int(salary) * 20 / 100

else:
    tax = int(salary) * 10 / 100

netsalary = int(salary) - tax
print("Employe name",name)
print("Employee Basic",salary)
print("-------------------------------------")
print("Tax calculated", tax)
print (" your salary is: " ,netsalary)

