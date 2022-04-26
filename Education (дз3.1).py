while True:
    mon=int(input("Дай 10 коп "))
    if mon==10:
        print("Привіт, ти можеш вирішити 3 завдання")
        n_r=3
        while n_r>0:
            print ("у тебе залишилося ",n_r,"рівнянь")
            a=float(input("a= "))
            b=float(input("b= "))
            c=float(input("c= "))
            if a==0:
                print("а не може дорівнювати нулю!")
            else:
                n_r=n_r-1
                d=b**2-4*a*c
                print(d)
                if d<0:
                    print ("коренів немає")
                elif d==0:
                    x= -b/(2*a)
                    print ("x=",x)
                else:
                    x1=(-b-d**0.5)/(2*a)
                    x2=(-b+d**0.5)/(2*a)
                    print ("x1=",x1)
                    print ("x2=",x2)
            #кінець розразунку
    elif mon==999:
        print ("Hi, admin")
        break
    else:
        print ("Ти кидаєш не ту монету")
print ("ввімкнено режим адміністратора")
    

