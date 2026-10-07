nr=int(input("Enter a number between 1 and 10: > "))
while nr>10 or nr<1:
    print("That number is out of range!")
    nr=int(input("Enter a number between 1 and 10: > "))
print(f"You entered: {nr}")