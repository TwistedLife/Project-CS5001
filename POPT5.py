def view_roles():

    print("Below are the roles:\n")
    print("1. Top")
    print("2. Jungle")
    print("3. Mid")
    print("4. ADC: Attack Damage Carry ")
    print("5. Support\n")
    select = int(input("Please select a role: "))
    if select == 1:
        print('''Typically, the top lane is the solo lane, with the other two team members trying to gain a foothold in the bottom lane. The narrower distance between lanes demands more care against sudden ganks.''')
    elif select == 2:
        print('''Jungling is the action of killing neutral "monsters", which are creatures located between the lanes in Summoner's Rift. The Jungle is the part of the Summoner's Rift that is not occupied by lanes or team's bases, including the river that divides it. Junglers rely on killing neutral monsters in the jungle to keep up with their laning teammates in terms of gold and experience. In a standard 5-on-5 game of League of Legends, four players in each team are laners, and one player is the jungler.''')
    elif select == 3:
        print('''Mid laners are champions that dwell in the mid lane. Your mid lane player is the core of any team and is arguably the most difficult role to play in League of Legends. This is due to the amount of game knowledge needed to perform well in the role.''')
    elif select == 4:
        print('''The ADC (also known as “Marksman”) is a role traditionally dedicated to the long-ranged carry. As an ADC, you'll be expected to focus on farming up to get your items as fast as possible. You'll be squishy and weak early on, but in exchange, you'll be extremely powerful later on in the game.''')
    elif select == 5:
        print('''The Support role is all about making sure things run smoothly for your team. You help facilitate vision control, protect your ADC, and provide game-changing crowd control. You won’t be the one carrying your team with kills or clutch Smite steals, but you’ll be the one who enables your ADC to get that Quadra-kill and you’ll be the one who sets up the vision that let’s your Jungler make that steal.''')

