
try:
    gross = float(input("Enter your salary: "))
    children = int(input("Enter the number of children you have: "))

except ValueError:
    print("Your salary or number of children must be expressed in a number format.")

else:
    if gross < 0:
        print("?")
    elif gross < 1000 and gross > 0:
        net = (0.9 + 0.01*children) * gross
        print("Your salary is ", net)
    elif gross < 2000 and gross >= 1000:
        net = (0.88+ 0.01*children) * gross
        print("Your salary is ", net)
    elif gross < 4000 and gross >= 2000:
        net = (0.86 + children*0.005) * gross
        print("Your salary is ", net)
    elif gross >= 4000:
        net = (0.82 + children*0.005) * gross
        print("Your salary is ", net)

