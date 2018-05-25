class User:
    name = ""
    gender = ""
    rate = 0
    need = 0
    # define default init func
    def __init__(self, name, age, gender, weight, height, activity):
        self.name = name
        self.age = age
        self.gender = gender
        self.weight = weight
        self.height = height
        self.activity = activity

    # calculate the user's BMR (Basal Metabolic Rate)
    def bmr(self):
        # if the user is male, use the bmr formula for men
        if self.gender == "m":
            User.rate = 66 + (6.23 * self.weight) + (12.7 * self.height) - (6.8 * self.age)
        # if the user is female, use the bmr formula for women
        if self.gender == "f":
            User.rate = 655 + (4.35 * self.weight) + (4.7 * self.height) - (4.7 * self.age)
        # print the user's bmr
        print(User.rate)
    # calculate the user's total daily calorie needs using the Harris Benedict equation
    def daily_cal(self):
        # if the user is sedentary, use this formula
        if self.activity == 1:
            User.need = User.rate * 1.2
        # if the user is lightly active, use this formula
        if self.activity == 2:
            User.need = User.rate * 1.375
        # if the user is moderately active, use this formula
        if self.activity == 3:
            User.need = User.rate * 1.55
        # if the user is very active, use this formula
        if self.activity == 4:
            User.need = User.rate * 1.725
        # if the user is extra active, use this formula
        if self.activity == 5:
            User.need = User.rate * 1.9
        # print the user's total daily calorie needs
        print(User.need)

# user information
quan = User("Quan", 18, "m", 132, 68, 3)

# calculate this user's bmr
quan.bmr()
quan.daily_cal()



