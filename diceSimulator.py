import random
# l = random.randint(1, 6)
# l = [1, 2, 3, 4, 5, 6]
print("1.Want to play more... 2.Exit... ")

while True:
    user = int(input("Enter your choice "))
    if user == 1:
        # botInput = random.choice(l)
        botInput = random.randint(1, 6)
        print("you got ", botInput)
    elif user > 2:
        print("invalid choice")
    else:
        break
