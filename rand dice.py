import random

dice = random.randint(1, 10)

k = 0
s = dice
while s != 100:
    dice = random.randint(1, 10)
    print(dice)
    s += dice
    if s > 100:
        s = 0
        k += 1
print("Кількість", k, s)
