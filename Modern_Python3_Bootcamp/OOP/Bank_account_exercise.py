
class BankAccount:
    
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0.0
        
    def deposit(self, amount):
        self.balance += amount
        return f"{self.owner}'s account has increased to {self.balance}."
    
    def withdraw(self, amount):
        self.balance -= amount
        return f"{self.owner}'s account has decreased to {self.balance}."
    
    
account1 = BankAccount("Darcy")
print(account1.deposit(500))
print(account1.withdraw(250.50))
    