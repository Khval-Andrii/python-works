matr=[]
for i in range(0,5):
    matr.append ([])
    for j in range (0,3):
        matr[i].append (str(j)+"-"+str(i))
for j in range (0,3):
    for i in range (0,5):
        print(matr[i][j], end=' ')
    print()
print("="*40)

matr=[]
for i in range(0,5):
    matr.append (input("введіть число"))
    for j in range(0, 3):
        pass
print(matr)

print("="*40)
s_inp=[]
for i in range(0,5):
    s_inp.append([])
    for j in range (0,3):
        s_inp[i].append(int(input("Введіть елемент стовбчика №"+str(i+1)+" ")))

for j in range(0,3):
    for i in range(0,5):
        print(s_inp[i][j], end=' ')
    print()




