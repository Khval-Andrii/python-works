apl = ["Лохов","Андропов","Кириченко","Янович","Хваль","Мотузяк"]
print (apl)
per=34
while per>0:
    per=0
    for i in range (0, len(apl)-1):
        if apl[i]>apl[i+1]:
            apl[i],apl[i+1]=apl[i+1],apl[i]
            per=per+1
    print(apl)
print("відсортований масив")
print(apl)
