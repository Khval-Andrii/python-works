import random
a=int(input("Виберіть перше число від 1 до 9 "))
b=int(input("Виберіть друге число від 1 до 9 "))
c=int(input("Виберіть третє число від 1 до 9 "))
r1=random.randint(1,9)
r2=random.randint(1,9)
r3=random.randint(1,9)
bal=0
bal1=0
bal2=0
bal3=0
print("Гравець вибрав числа: ", a, b, c, ", а з лото випали числа: ", r1, r2, r3)
if (a==r1) and (b==r2) and (c==r3):
    bal=500
    print("Джек-пот: ", bal)
if a==r1:
    bal1=bal1+100
elif (a==r2) or (a==r3):
    bal1=bal1+10       
if b==r2:
    bal2=bal2+100
elif (b==r1) or (b==r3):
    bal2=bal2+10
if c==r3:
    bal3=bal3+100
elif (c==r1) or (c==r2):
    bal3=bal3+10
bal=bal1+bal2+bal3

print("Ваш виграш складає: ", bal)

