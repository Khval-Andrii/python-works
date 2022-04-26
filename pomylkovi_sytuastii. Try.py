s_inp = []
i = 0
while True:
    try:
        el = int(input("введіть елемент №" + str(i + 1) + " "))
        s_inp.append(el)
        if input("Для введення наступного елементу натисни Ентер. Для завершення - будь який елемент") != "" \
                                                                                                          "":
            break
        else:
            pass
    except ValueError:
        print("Ви помилилися. Введіть ціле число!!!")
        continue
    i = i + 1
print(s_inp)
