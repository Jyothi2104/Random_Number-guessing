import random
a = random.randint(1,100)
total = 0

while True:
    total = total + 1
    b = int(input("guess your number between 1 - 100 :- "))

    if b == a:
        print(f"congratulations you have won  in {total} tries!")
        break

    elif b > a:
        print("sorry wrong guess go lower !")

    elif b < a:
        print("sorry wrong guess go higher !")