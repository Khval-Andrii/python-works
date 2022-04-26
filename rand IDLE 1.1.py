import random
bal=0
for q in range(12):
    a=random.randint(1,9)
    b=random.randint(1,9)
    print("Скільки буде", a,"*", b,"=?")
    n=int(input())
    if n==a*b:
        print("Правильно")
        bal+=1
    else:
        print("Неправильно")
print("Оцінка", bal)
