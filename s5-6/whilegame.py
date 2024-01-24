import random
lives = 3

while lives:
    print("you have", lives, "lives left")
    dice_roll = random.randint(1, 6)
    if dice_roll == 6:
        print("you rolled a 6, you win!")
        break

    print("you rolled a", dice_roll, "try again")
    lives -= 1

else:
    print("You lost all your lives, game over")


#While True loop (infinite loop) is useful when you don't know how many iterations will be needed
#While True needs a break, and can make use of continue operator

