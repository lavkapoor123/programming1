print("Let's see who has the highest card!")
player1=int(input("Player 1, enter your card: > "))
player2=int(input("Player 2, enter your card: > "))
if(player2>player1):
    print("Player 2 has the highest card!")
elif(player1>player2):
    print("Player 1 has the highest card!")
else:
    print("Both players are holding the same value card!")