
try:
    salary = int(input("Enter your salary: "))

except ValueError:
    print("Your salary must be a number")

else:
    if salary < 0:
        print("Are you in debt or are you stupid?")
    elif salary > 1000:
        