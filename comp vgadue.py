start = 1
finish = 10
guess = (start + finish)//2
print("Мій варіант ", guess)
user = input("Ок, багато, мало? ")
while user !="Ок":
    if user == "багато":
        finish = guess
    else:
        start = guess
    guess = (start + finish) // 2
    print("Мій варіант ", guess)
    user = input("Ок, багато, мало? ")