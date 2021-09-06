import random
secretNUM = random.randint(1,30)
print("hmm mai ek number sochta hu")
 #ask the player to guess 6 times
for guesstake in range (1,7):
    print("take a guess")
    guess = int(input())

    if guess > secretNUM:
        print("jyada number mat soch ")
    elif guess < secretNUM:
        print("chhoti soch k aadmi kuch bada soch")
    else:
        break
if guess == secretNUM:
    print("mauj krdi bete")
else:
    print("bhagg ","mai ",secretNUM," soch rha tha")