nr=int(input("Game master, enter a number: > "))
player=int(input("Player, guess the number: > "))
while player!=nr:
    if(player<nr):
        print("Your guess is too low!")
        print("Try again!")
    if(player>nr):
        print("Your guess is too high!")
        print("Try again!")
    player=int(input("Player, guess the number: > "))
print("You guessed correctly!")
    