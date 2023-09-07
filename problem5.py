class BankAccount:
    
    # Constructor
    def __init__(self, account_name, starting_balance):
        self.name = account_name
        self.balance = starting_balance
    
    # Deposit money into account
    def deposit(self, money):
        self.balance = self.balance + money
        print("Deposited", money)
    
    # Withdraw money from account
    def withdraw(self, money):
        if money > self.balance:
            print("Not enough money!")
        else:
            self.balance = self.balance - money
            print("Withdrew", money)
    
    # Get the account balance
    def get_balance(self):
        return self.name + " has a balance of " + str(self.balance)


# Create a new bank account
my_account = BankAccount("My Account", 100)

# Deposit and withdraw money
my_account.deposit(50)
my_account.withdraw(25)

# Print out the balance
print(my_account.get_balance())
