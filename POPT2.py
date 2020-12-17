def view_items():
    
    print("Here is the list of items below:\n")
    f = open("items.txt","r")
    print(f.read())
    f.close()
    print("Pick an option: ")
    print("1. Learn about an item")
    print("2. Main menu")
    opt2 = int(input("What is your choice? "))
    if opt2 == 1:
        print("Select from 1 of the 10 Mythic items below: ")
        print("1. Duskblade of Draktharr")
        print("2. Eclipse")
        print("3. Galeforce")
        print("4. Hextech Rocketbelt")
        print("5. Kraken Slayer")
        print("6. Liandry's Anguish")
        print("7. Luden's Tempest")
        print("8. Night Harvester")
        print("9. Stridebreaker")
        print("10. Trinity Force")
        num = int(input("Which Mythic item do you pick? "))
        if num == 1:
            print("Stats: +20 ability haste, +55 attack damage")
            print("Passive: +18 Lethality (11.2 − 18 (based on level) armor penetration)")
            print("UNIQUE – NIGHTSTALKER: Basic attacking an enemy champion deals 100 (+ 30% bonus AD) bonus physical damage on-hit and slows them by 99% for 0.25 seconds (15 second cooldown). Champion takedowns within 3 seconds reset this effect's cooldown and grant you invisibility for 1.5 seconds.")
            print("MYTHIC PASSIVE: Empowers your other Legendary items with 5 ability haste.")
        elif num == 2:
            print("Stats: +55 attack damage, +10% omnivamp")
            print("Passive: +18 Lethality (11.2 − 18 (based on level) armor penetration)")
            print("UNIQUE – EVER RISING MOON: Hitting an enemy champion with 2 separate attacks or abilities within 1.5 seconds deals 6% of target's maximum health as bonus physical damage and grants you 15% bonus movement speed and a shield for 2 seconds.")
            print("MYTHIC PASSIVE: Empowers your other Legendary items with 4% armor penetration.")
        elif num == 3:
            print("Stats: +60 attack damage, +20% attack speed, +20% critical strike chance")
            print("Passive: MYTHIC PASSIVE: Empowers your other Legendary items with 3% bonus movement speed.")
            print("Active: UNIQUE – CLOUDBURST: Dash to the target location (450 range, 200 minimum), though not through terrain, and fire three homing missiles at the enemy with the most missing health within ~750 radius of you at the end of the dash, prioritizing enemy champions. Each missile deals 60 − 105 (based on level) (+ 15% bonus AD) magic damage, for a total of 180 − 315 (based on level) (+ 45% bonus AD), increased by 0% − 50% (based on target's missing health) (60 second cooldown).")
        elif num == 4:
            print("Stats: +80 ability power, +15 ability haste, +250 health")
            print("Passive: MYTHIC PASSIVE: Empowers your other Legendary items with 5 magic penetration.")
            print("Active: UNIQUE – SUPERSONIC: Dash in the target direction, though not through terrain, unleashing an arc of rockets that deal 175 − 250 (based on level) (+ 15% AP) magic damage. Then, gain 50% bonus movement speed toward enemy champions for 2 seconds (40 second cooldown). Supersonic resets the user's basic attack timer.")
        elif num == 5:
            print("Stats: +65 attack damage, +25% attack speed, +20% critical strike chance")
            print("Passive: UNIQUE – BRING IT DOWN: Basic attacks on-attack grant a stack for 3 seconds, up to 2 stacks. At 2 stacks, the next basic attack consumes all stacks on-attack to deal 60 (+ 45% bonus AD) bonus true damage on-hit.")
            print("MYTHIC PASSIVE: Empowers your other Legendary items with 10% bonus attack speed.")
        elif num == 6:
            print("Stats: +80 ability power, +20 ability haste, +600 mana")
            print("Passive: UNIQUE – TORMENT: Dealing ability damage burns enemies, causing them to take 60 (+ 6% AP) (+ 4% target's maximum health) magic damage over 4 seconds and the user to ignore 5% of their magic resistance for the duration, increasing by 5% per second over the duration, up to 15%.")
            print("MYTHIC PASSIVE: Empowers your other Legendary items with 5 ability haste.")
        elif num == 7:
            print("Stats: +80 ability power, +20 ability haste, +600 mana, +6 magic penetration")
            print("Passive: UNIQUE – ECHO: Dealing ability damage to an enemy deals 100 (+ 10% AP) bonus magic damage to your target and 3 nearby enemies and grants you 15% bonus movement speed for 2 seconds (10 second cooldown).")
            print("MYTHIC PASSIVE: Empowers your other Legendary items with 5 magic penetration.")
        elif num == 8:
            print("Stats: +80 ability power, +15 ability haste, +250 health")
            print("Passive: UNIQUE – SOULREND: Damaging an enemy champion deals 125 − 200 (based on level) (+ 15% AP) bonus magic damage and grants you 25% bonus movement speed for 1.5 seconds, with the duration extending upon damaging new champions (40 second cooldown per champion).")
            print("MYTHIC PASSIVE: Empowers your other Legendary items with 5 ability haste.")
        elif num == 9:
            print("Stats: +10 ability haste, +50 attack damage, +20% attack speed, +300 health")
            print("Passive: UNIQUE – HEROIC GAIT: Dealing physical damage grants you 30 bonus movement speed for 2 seconds.")
            print("MYTHIC PASSIVE: Empowers your other Legendary items with 3% bonus movement speed.")
        elif num == 10:
            print("Stats: +10 ability haste, +35 attack damage, +35% attack speed, +200 health")
            print("Passive: UNIQUE – THREEFOLD STRIKE: Basic attacks grant 25 bonus movement speed for 3 seconds. If the target is a champion also increases base attack damage by 6% for the same duration, stacking up to 5 times for a 30% increase.")
            print("UNIQUE – SPELLBLADE: After using an ability, your next basic attack within 10 seconds deals 200% base AD bonus physical damage on-hit (1.5 second cooldown, begins after using the empowered attack).")
            print("MYTHIC PASSIVE: Empowers your other Legendary items with 10% bonus attack speed.")
    
            
            
        
