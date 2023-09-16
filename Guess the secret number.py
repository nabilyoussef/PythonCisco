secret_number = 777
guessNum=0
print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")
while guessNum==0:
    guessNum= int(input("\n Guess the secret numeber: "))
    if(guessNum==secret_number):
        print("Well done, muggle! You are free now.")
    else:
        print("Ha ha! You're stuck in my loop!")
        guessNum=0