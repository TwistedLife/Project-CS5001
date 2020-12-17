def roster():
    
    print("Time to create a roster!")
    blanklist = []
    for i in range(5):
        added = input("Which champ will you add? ")
        blanklist.append(added)
    print("Here is your team:")
    print(blanklist)
    blanklist2 = []
    for i in range(5):
        added2 = input("Who is enemy team? ")
        blanklist2.append(added2)
    print("This is the enemy team:")
    print(blanklist2)
