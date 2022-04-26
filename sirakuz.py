a = int(input("Введіть число "))
s = a
while s != 1:
    if s % 2 == 0:
        s = s / 2
    else:
        s = ((s * 3) + 1) / 2
    print(int(s), end=" ")
print("maza faka")