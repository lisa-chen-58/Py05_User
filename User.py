
class User:
    # class attributes get defined in the class 
    bank_name = "First National Dojo"
    
    # now our method has 2 parameters!
    def __init__(self, name, email_address):
        self.name = name #instance attribute
        self.email = email_address #instance attribute
        self.account_balance = 0 #instance attribute

    def make_deposit(self, amount): #takes an argument that is the amount of the deposit
        self.account_balance += amount

#calling the User function
guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")

print(guido.name)	# output: Guido van Rossum
print(monty.name)	# output: Monty Python

guido.make_deposit(100)
guido.make_deposit(200)
monty.make_deposit(50)
print(guido.account_balance)	# output: 300
print(monty.account_balance)	# output: 50


