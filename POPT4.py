def view_maps():

    print("Here are the available maps:")
    print("Map 1: Classic (2 maps)")
    print("Map 2: Howling Abyss (Aram)")
    print("Map 3: URF: Ultra Rapid Fire")
    print("Map 4: TFT: Team Fight Tactics")
    opt2 = int(input("Which map are you interested in? "))
    if opt2 == 1:
        print("Classic has Summoners Rift (1) and Twisted Treeline (2).")
        option = int(input("Which one do you want to learn about? "))
        if option == 1:
            print('''The objective of Summoner's Rift is simple – destroy the enemy nexus. In order to do this, champions must traverse down one of three different paths (or lanes) in order to attack their enemy at their weakest points they can exploit. Both teams have their lanes defended by numerous turrets; each turret grows in strength the closer it gets to its respective nexus and each turret must be eliminated in order to gain access to the next turret in that lane. Cooperating with fellow summoners is an absolute requirement for success, as it is easy for a champion to find themselves ambushed by enemies in the lanes of the Rift.''')
        elif option == 2:
            print('''A smaller map than Summoner's Rift, the Twisted Treeline is configured horizontally, with two lanes flanking a neutral area. Turrets are placed along the length of each lane, and the nexus is defended by a single turret. Teams are composed of three champions apiece, and each champion spawns with a substantial sum of gold. The reduced map size and accelerated level curve makes for a shorter game length and higher kill scores.''')
    elif opt2 == 2:
        print('''The objective of Howling Abyss is simple: destroy the enemy nexus. In order to do this, champions must traverse down one path (or lane) in order to attack their enemy at their weakest points they can exploit. Both teams have their lane defended by numerous turrets; each turret grows in strength the closer it gets to its nexus and each turret must be eliminated in order to gain access to the next turret in that lane. Cooperating with fellow summoners is an absolute requirement for success, as it is easy for a champion to find themselves ambushed by enemies in the lanes of the Abyss.''')
    elif opt2 == 3:
        print('''Ultra Rapid Fire (U.R.F.) is a Featured Game Mode that was first introduced for April Fools' Day that, in a nutshell, grants all players 80% cooldown reduction and removes ability costs. The mode has since been succeeded by All Random Ultra Rapid Fire (A.R.U.R.F.), which follows the same gameplay but now utilizes the All Random draft type instead of Blind With Bans. To celebrate the 10th Anniversary of League of Legends' release, U.R.F. was brought back as an experiment.''')
    elif opt2 == 4:
        print('''The Arena is the island that encompasses the battlefield of Teamfight Tactics, which includes the battlefield for champions to fight, the champion bench, and the Gold Generators.Each player has their own arena map and each player travels to another players map or attacks from their own arena depending on the round.''')
            

