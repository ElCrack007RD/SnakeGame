import random
guessesTaken = 0
minNumber = 1
maxNumber = 20
print("Hellow, what is your name?:")
username = input()
print("Bienvenido a el juego a Pensar, donde te llevaremos al limite")
number = random.randint(minNumber,maxNumber)   
print("Well," + username + ',I am thinking in a number between ' + str(minNumber) + ' and ' + str(maxNumber))
while guessesTaken < 6:
    print("Take a guess:")
    guess = input()
    guess = int(guess)
    guessesTaken = guessesTaken + 1
    if guess < number:
        print("Your guess is too low.")
    if guess > number:
        print("Your number is too hight.")
    if guess == number:
        break
if guess == number:
        guessesTaken = str(guessesTaken)
        print("Good Job." + username + '!You guessed my number in ' + guessesTaken + ' guesses ')
if guess != number:
        number = str(number)
        print("No, the number i was thinking of was " + number)
