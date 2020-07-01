import random

def guessgame():
    number=int(random.randint(1,100))
    attempt=5
    while attempt!=0:
        guess=int(input("Enter your guess number:\n"))
        if guess==number:
            attempt -=1
            print(f"you have won in {5-attempt} attempts!")
            print(f"{number} is correct")
            break
        elif guess>number:
            print("your guess is a high number try with a lower one")
            attempt -=1
        else:
            print("your guess is a low number try with a higher one")
            attempt -=1
        print(f"attempt left:{attempt}")
    if guess!=number: 
         print("\nyou loss due to out of attempt!")
         print(f"correct number is {number}")
                       
ch="y"  
print("____________________GUESS GAME____________________\n")    
print("Guess the number between 1 to 100 and you have 5 attempts!\n")     
while ch=="y":
    guessgame()

    ch=input("\nDo you want to play again(y/n):\n")
            