import random

draws = []
for i in range(6):
    number = random.randint(1,50)
    while number in draws:
        number = random.randint(1, 50)
    draws.append(number)
draws.sort()
print("Your Lottery Numbers are:")
print(draws)