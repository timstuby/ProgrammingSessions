

insertnum = int(input("Enter a number:"))

def divisor(insertnum):
    divisors = []
    for i in range(1, insertnum+1):
        if insertnum % i == 0:
            divisors.append(i)
    return divisors

print(divisor(insertnum))

