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
            return self;
        else:
            self.is_rewards_member = True;
            self.gold_card_points = 200;
            return self;

    def spend_points(self,amount):
        if(self.is_rewards_member == False):
            print(f"{self.first_name} is not a rewards member, please enroll")
            return self;
        elif(self.gold_card_points < amount):
            print(f"{self.first_name} only has {self.gold_card_points} points left")
            return self;
        elif(self.gold_card_points > 40):
            return self;
            print(f"{amount} is too high! You can only spend up to 40 points")
        else:
            # have this method decrease the user's points by the amount specified.
            self.gold_card_points -= amount;
            return self;

lisa = User("Lisa","Chen","lisa@email.com",30)
lisa.display_info().enroll()
print("")
bryan = User("Bryan","Konya","bryan@email.com",30)
bryan.spend_points(50).display_info()
print("")
saria = User("Saria","Chen","saria@email.com",13)
saria.enroll().display_info().spend_points(80).gold_card_points;


