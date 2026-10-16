
print("Welcome to your todo app!")

todo = "Your most important todo is: nothing in particular"

question = input("Do you want to change (C) your todo-item, show (S) your current item or Exit (E) the application? > ")

while question != "E":
    if question == "S":
        print(todo)

    if question == "C":
        new_todo = input("Type your todo: > ")
        todo = "Your most important todo is: " + new_todo

    question = input("Do you want to change (C) your todo-item, show (S) your current item or Exit (E) the application? > ")
