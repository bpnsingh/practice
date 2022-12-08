
# Test program using accounts
# Version 2, using a list of accounts

# Bring in all the code from the Account class file
from Accounts import *

# Start off with an empty list of accounts
accountsList = [ ]

# Create two accounts
oAccount = Account('Joe', 100, 'JoesPassword')
accountsList.append(oAccount)
print("Joe's account number is 0")

oAccount = Account('Mary', 12345, 'MarysPassword')
accountsList.append(oAccount)
print("Mary's account number is 1")

accountsList[0].show()
accountsList[1].show()
print()

# Call some methods on the different accounts
print('Calling methods of the two accounts ...')
accountsList[0].deposit(50, 'JoesPassword')
accountsList[1].withdraw(345, 'MarysPassword')
accountsList[1].deposit(100, 'MarysPassword')

# Show the accounts
accountsList[0].show()
accountsList[1].show()

