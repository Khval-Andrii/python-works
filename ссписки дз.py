import random

spysok = []

for i in range(10):
    k = random.randint(1, 5)
    spysok.append(k)
print(spysok)
big=5
pos_sp = []
position = 0
for i in range(10):
    if spysok[i]>=big:
        big=spysok[i]
        position=i
        pos_sp.append(position)
#position=spysok.index(big)

print("Максисальне значення= ", big)
print("індекс максисального значення= ", position,)
print("Список індексів максисального значення= ", pos_sp)
print("-"*40)



