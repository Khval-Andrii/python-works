import random

comp = random.randint(1, 10)
user = int(input("Ваша версія="))
while user != comp:
    if user < comp:
        print("Мало")
    elif user > comp:
        print("Багато")
    user = int(input("Ваша версія="))
print("Число вгадано!")
