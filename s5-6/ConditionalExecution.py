import random
drinks = ["beer", "wine", "whiskey", "rum", "gin tonic", "vodka", "martini", "rakia"]
try:
    age = int(input("How old are you? "))
    country = input("Where you living??")
except ValueError:
    print("I am sorry, but that is not a valid number")

else:
    # Do some sanity checks on age
    if age < 0 or age > 130:
        print("I am sorry, but your age cannot be negative or greater than 130")
    elif age < 18:
        print("I am sorry, too young to play this drinking game everywhere")
    elif age < 21 and country == "US":
        print("I am sorry, too young to play this drinking game in the US")
    else:
        drink = random.choice(drinks)
        print("Take a shot of ", drink, ". Thank you for playing, you are", age, "years old")
