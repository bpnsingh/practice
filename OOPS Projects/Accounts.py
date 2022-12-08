class Account:
    def __init__(self,name, balance,password):
        self.name = name
        self.balance = int(balance)
        self.password = password

    def deposit(self,amount,password):
        if self.password == password:
            self.balance += amount
            return self.balance
        else:
            print("password mismatch")

    def withdraw(self,amount,password):
        if self.password == password:
            self.balance -= amount
            return self.balance
        else:
            print("password mismatch")

    def getBalance(self,password):
        if self.password == password:
            return self.balance

    def show(self):
        print ("{0} has {1} . password is {2}".format(self.name, self.balance, self.password))


