print("Welcome to the museum!")
def calculateprice():
    age=int(input("What is your age? > "))
    cost=0
    if(age<6):
        cost+=0
        print("Your ticket is free!")
    elif (age<18):
        cost+=4
        print("Your ticket costs "+str(cost)+" EUR.")
    elif (age<65):
        cost+=12
        print("Your ticket costs "+str(cost)+" EUR.")
    else:
        cost+=7
        print("Your ticket costs "+str(cost)+" EUR.")
        
calculateprice()