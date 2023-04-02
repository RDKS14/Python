bill=input("How much is the bill?")
paid=input("How much paid?")
balance = int(paid) - int(bill)
print("Your balance is:" ,balance)
if balance>=50:
    print("50£:",int(balance/50))
    balance = balance %50
if balance>=20:
    print("20£:",int(balance/20))
    balance = balance %20
if balance>=10:
    print("10£:1" )
    balance = balance %10
if balance >= 5:
    print("5£:1")
    balance = balance % 5
if balance >= 2:
    print("2£", int(balance / 2))
    balance = balance % 2
if balance>=1:
    print("1£:1")
