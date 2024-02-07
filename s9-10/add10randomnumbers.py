
#add 10 random numbers and prints the answer
import random
john = "1234567890"
zulu = 0
for i in john:
    i = random.randint(1,1000)
    zulu += i
print(zulu)