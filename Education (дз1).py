for portsiy in range(1, 10):
    s = portsiy * 4.75
    a = float(portsiy % 10)
    g = s // 1
    k = s % 1 * 100
    b = g % 10
    c = g // 10

    if b == 1 and c != 1:
        b = "гривня"
    elif (b == 2 or b == 3 or b == 4) and (c != 1):
        b = "гривні"
    else:
        b = "гривень"
    if a == 1:
        print(portsiy, "порція", "коштує", int(g), str(b), int(k), "копійок")
    elif a == 0:
        print(portsiy, "порцій", "коштують", int(g), str(b), int(k), "копійок")
    elif a < 5:
        print(portsiy, "порції", "коштують", int(g), str(b), int(k), "копійок")
    else:
        print(portsiy, "порцій", "коштують", int(g), str(b), int(k), "копійок")

print('-' * 40)
