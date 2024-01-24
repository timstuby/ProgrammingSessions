try:
    age1 = int(input("What is your age player 1? "))
    age2 = int(input("What is your age player 2? "))
    res = age1 / age2
except ValueError:
    print("I am sorry, but that is not a valid number")
except ZeroDivisionError:
    print("Do not put zero!!")
except:
    print("I am sorry, but now you must die")
else:
    print("Player 1 is older than player 2 by a factor of", res)
finally:
    print("Thank you for playing")