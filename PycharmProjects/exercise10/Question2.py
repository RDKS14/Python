print("Welcome to Smiths Banking ltd")
print("please insert your card")

card = None
while card != 'done':
    card = input("Please type done when your card is inserted")


print("now insert your 4 digit pin below")


pincode = int(4355)
for i in range (3, 0, -1):
    pin = int(input(""))
    if pin == pincode:
        break
    else:print("Incorrect please try again")

if i == 1:
    print("You have been Denied Access")
else:
    print("Welcome to your account")
