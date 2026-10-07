attempts = 0
gamenr = int(input("Game master, enter a number: > "))

while attempts < 3:
    playernr = int(input("Player, guess the number: > "))
    attempts += 1

    if playernr > gamenr:
        print("Your guess is too high!")

    elif playernr < gamenr:
        print("Your guess is too low!")

    else:
        print("You guessed correctly!!")
        break

    if attempts < 3:
        print(f"Try again! (You have {3 - attempts} guesses left)")

else:
    print("You lose")