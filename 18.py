class bank:
    def __init__(self):
        self.accno=int(input("enter your accno:"))
        self.acctype=(input("enter your acctype:"))
        self.holdname=(input("enter your name:"))
        self.balance=int(input("enter your balance:"))
    def deposit(self):
        amount=int(input("enter the amount to deposit:"))
        self.balance+=amount
        print("The account balance is:",self.balance)
    def withdraw(self):
        amount=int(input("Enter the amount to withdraw:"))
        if self.balance>=amount:
            self.balance-=amount
            print("YOU WITHDRAW RS:",amount)
        else:   
            print("INSUFFICIENT BALANCE TO WITHDRAW")
    def display(self):
            print("Net Available Balance is:",self.balance)


a=bank()
a.deposit()
a.withdraw()
a.display()
