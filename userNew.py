class User:
    def __init__(self, f_name, l_name, email, age):
        self.first_name = f_name
        self.last_name = l_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print(f"{self.first_name}\n{self.last_name}\n{self.email}\n{self.age}\n{self.is_rewards_member}\n{self.gold_card_points}")
        return self;

    def enroll(self):
        # Have this method change the user's member status to True and set their gold card points to 200.
        if(self.is_rewards_member == True):
            print("Already a rewards member")
        else:
            self.is_rewards_member = True;
            self.gold_card_points = 200;
            return self;

    def spend_points(self,amount):
        if(self.is_rewards_member == False):
            print(f"{self.first_name} is not a rewards member, please enroll")
        elif(self.gold_card_points < amount):
            print(f"{self.first_name} only has {self.gold_card_points} points left")
        elif(self.gold_card_points > 40):
            print(f"{amount} is too high! You can only spend up to 40 points")
        else:
            # have this method decrease the user's points by the amount specified.
            self.gold_card_points -= amount;


# In the outer scope, create a user instance and call the display_info method to test.
lisa=User("Lisa","Chen","lisa@email.com",30)
# print(lisa.display_info())

# Add the enroll method to the User class, implement and test by calling the method on the user in the outer scope.
# print (lisa.gold_card_points)
lisa.enroll()
# print (lisa.gold_card_points)

# Make 2 more instances of the User class.
bryan = User("Bryan", "Konya", "bryan@email.com", 30)
saria = User("Saria", "Chen", "saria@email.com", 13)

# Implement the spend_points(self, amount) method
# Have the first user spend 50 points
bryan.spend_points(50)

# Have the second user enroll.
saria.enroll()
saria.display_info()

# Have the second user spend 80 points
saria.spend_points(80)

# Call the display method on all the users.
lisa.display_info()
bryan.display_info()
saria.display_info()

