def best_teams():
    
    teamdic = {"FunPlus Phoenix": 0,"Invictus Gaming": 0,"G2 esports": 413,"SKT Telecom T1": 1150,"Griffin": 0,"Fnatic": 158,"Damwon Gaming": 1150,"Team Solo Mid": 201,"Royal Never Give Up": 0,"C9": 90,"Team Liquid": 150,"Flash Wolves": 0}
    mainlist = list(teamdic.values())
    print("Here is some good teams below:\n")
    z = open("teams.txt","r")
    print(z.read())
    z.close()
    pick1 = int(input("View teams above what ranking (ex: 100, 200 etc)? "))
    for key, value in teamdic.items():
        if value > pick1:
            print(key, value)
    if pick1 > 1150:
        print("None")
