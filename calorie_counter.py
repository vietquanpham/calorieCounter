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
        print("Without any activity, your body burns %s calories everyday" % User.rate)
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
        print("You need %s calories everyday in order to maintain your current weight" % User.need)

# user inserts their information
name = input("What is your name?")
age = int(input("How old are you?"))
gender = input("What is your gender? (m/f)")
weight = int(input("Enter your weight (pound)"))
height = int(input("Enter your height (inch)"))
activity = int(input("How active are you? (1: little or no exercise; 2: light exercise 1-3 days/week; 3: moderate exercise 3-5 days/week; 4: hard exercise 6-7 days/week; 5: very hard exercise & physical job or 2x training)"))
user = User(name, age, gender, weight, height, activity)

# calculate this user's bmr and total daily calorie needs
user.bmr()
user.daily_cal()





