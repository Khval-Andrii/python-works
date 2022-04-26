import random
moneta = random.choice(["орел", "решка"])
if moneta == "орел":
    print("Починає Аргентина")
else:
    print("Починає Ямайка")
a = random.randint(0, 5)
y = random.randint(0, 5)
print("Аргентина - Ямайка", a, ":", y)
if a == y:
    print("Нічия")
elif a > y:
    print("Перемогла Аргентина")
else:
    print("Перемогла Ямайка")


print("-"*40)

import random
k1=0
k2=0
for i in range (200):
    dice = random.choice(["Орел","Решка"])
    print(dice, end = " ")
    if dice == "Орел":
        k1+=1
    else:
        k2+=1
    
print("Статистика ", "Орел випав - ",k1, "Решка випала -", k2,)
