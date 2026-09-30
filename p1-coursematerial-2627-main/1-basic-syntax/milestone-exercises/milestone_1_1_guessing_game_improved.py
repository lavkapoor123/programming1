
player1=input("Player 1, enter an animal that player 2 needs to guess: > ")
player2=input("Player 2, what animal is player 1 thinking of? > ")
if(player2.lower()==player1.lower()):
    print("You guessed correctly!")
else:
    print("Nope, try again!")