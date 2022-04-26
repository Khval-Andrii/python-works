apl = [6,10,5,7,8,4]
print (apl)
max = apl[0]
min = apl[0]
max_i=0
min_i=0
sum=0
for i in range (0, len(apl)):
    print (apl[i])
    sum=sum+apl[i]
    if max<apl[i]:
        max=apl[i]
        max_i=i
    if min>apl[i]:
        min=apl[i]
        min_i=i
print ("Мінімальне значення масиву:",min,"номер ",min_i)
print ("Максимальне значення масиву :",max,"номер ",max_i)
print ("Сума всіх значень",sum)
print ("Середнє значення масиву",sum/len(apl))
