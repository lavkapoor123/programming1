print("Welcome to your todo app!")
todos=[]
question=input("Do you want to (A) add a new todo, remove (R) a todo, show (S) all your current todos or exit (E) the application? > ")
while question!="E":
    if (question=="A"):
        additem=input("Type your todo: > ")
        todos.append(additem)
    if question=="S":
        print(f"Your todos are: {todos}")
    if question=="R":
        removeitem=input("What todo do you want to remove? > ")
        if removeitem in todos:
            todos.remove(removeitem)

    question=input("Do you want to (A) add a new todo, remove (R) a todo, show (S) all your current todos or exit (E) the application? > ")

        
        