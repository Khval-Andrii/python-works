day = int(input("Введіть день "))
month = int(input("Введіть місяць "))
year = int(input("Введіть рік "))
leap = 0
day1=0
month1=0
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    leap == 1
else:
    leap == 0
k = 0
if month == 12:
    k = 31 - day

if month == 11:
    k = 31 + 30 - day

if month == 10:
    k = 31 + 30 + 31 - day

if month == 9:
    k = 31 + 30 + 31 + 30 - day

if month == 8:
    k = 31 + 30 + 31 + 30 + 31 - day

if month == 7:
    k = 31 + 30 + 31 + 30 + 31 + 31 - day

if month == 6:
    k = 31 + 30 + 31 + 30 + 31 + 31 + 30 - day

if month == 5:
    k = 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 - day

if month == 4:
    k = 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 - day

if month == 3:
    k = 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + 31 - day

if month == 2:
    k = 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + 31 + 28 - day + leap

if month == 1:
    k = 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + 31 + 28 + 31 - day + leap

if (k + day) > 256:
    day1 = (k + day) - 256
    month1 = (k + day)//30
    print("День програміста відзначають: ", day1,".",month1,".",year)
print("Залишилось", k, "днів")
print("З початку року пройшло", 365 + leap - k, "днів")

