

class Account:
    account_num = 0

    def __init__(self, initial):
        self._balance = initial
        Account.account_num += 1
        print("Your Account number: ", Account.account_num , "Your balance is: £", self._balance)

    def deposit(self, amt):
        self._balance += amt
        print( "you issued a deposit of: £ ", amt , "Your account balance is now: £" , self._balance)

    def withdraw(self,amt):
        self._balance -= amt
        print("You have withdrawn :£", amt, "Your account balance is :£", self._balance)

    def getbalance(self):
        return self._balance
