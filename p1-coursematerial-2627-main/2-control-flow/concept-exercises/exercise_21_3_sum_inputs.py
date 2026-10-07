nr=int(input("Enter a number (0 to stop): > "))
sum=0
while nr!=0:
    sum+=nr
    nr=int(input("Enter a number (0 to stop): > "))
    
print(f"Total: {sum}")