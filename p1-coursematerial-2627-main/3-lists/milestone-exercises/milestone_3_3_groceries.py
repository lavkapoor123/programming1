print("Welcome to your groceries app!")
groceries=[]
question=input("Do you want to (A) add new groceries, remove (R) groceries, show (S) all your current groceries or exit (E) the application? > ")
while question!="E":
    if question=="A":
        add=input("What do you want to add?: > ")
        for item in add.split(","):
            item = item.strip()
            if item and item not in groceries:
                groceries.append(item)
    if question=="S":
        print(f"Your groceries list is: {groceries}")
    if question=="R":
        rem=input("What do you want to remove?: > ")
        for item in rem.split(","):
            item = item.strip()
            if item in groceries:
                groceries.remove(item)

    question=input("Do you want to (A) add new groceries, remove (R) groceries, show (S) all your current groceries or exit (E) the application? > ")

    
