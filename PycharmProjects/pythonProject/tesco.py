product = input("Enter the product")
quantity = input("Enter the Quantity")
price = input("Enter the Unit Price")
bill = int(quantity)*float(price)
Vat = bill*20/100
print( "***Welcome to Tesco***")
print ("product purchased:",product)
print ("Quantity", quantity)
print ("unit price: £", price)
print("Total unit price", bill)
print ("Total VAT", Vat)
print("-----------------------")
print("your Bill is : £",bill + Vat)