import random
Playing=True
number=(random.randint(1,5))
print ("Welcome to the guessing game")
print ("You are in easy mode")
print ("Guess a number from 1 to 5")
print ("Good luck")
while Playing:
    Guess=int(input ("What is your Guess " ))
    if number==Guess:
        print ("Congratuations you have won you have now unlocked medium dificulty")
        print (number)
        break
    else:
        print ("Incorect try again")
        print (number)