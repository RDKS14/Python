bill = input("how much is the bill")
paid = input("how much have you paid")
balance = int(paid) - int(bill)
print("your balance is", balance)

if balance>=50:
    print("50=",int(balance/50))
    balance= balance%50

if balance >= 20:
    print("20=",int(balance/20))
    balance = balance % 20

if balance >= 10:
    print("10=", int(balance / 10))
    balance = balance % 10

if balance >= 5:
    print("5=", int(balance / 5))
    balance = balance % 5

if balance >= 2:
    print("2=", int(balance / 2))
    balance = balance % 2

if balance >= 1:
    print("1=1")
    balance = balance % 1