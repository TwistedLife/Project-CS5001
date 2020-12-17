from POPT1 import view_champs
from POPT2 import view_items
from POPT3 import roster
from POPT4 import view_maps
from POPT5 import view_roles
from POPT6 import learn_more
from POPT7 import best_teams
def main():
        
        status1 = False
        while status1 == False:
            print("Please select from the menu below: \n")
            print("Option 1: View champions")
            print("Option 2: View all items")
            print("Option 3: Create a roster")
            print("Option 4: View maps")
            print("Option 5: View roles")
            print("Option 6: Learn more")
            print("Option 7: Check best teams")
            print("Option 8: Quit \n")
            opt = int(input("Which option will you select? "))
            if opt == 1:
                    view_champs()
            elif opt == 2:
                    view_items()
            elif opt == 3:
                    roster()
            elif opt == 4:
                    view_maps()
            elif opt == 5:
                    view_roles()
            elif opt == 6:
                    learn_more()
            elif opt == 7:
                    best_teams()
            elif opt == 8:
                    break
            else:
                print("Not a valid option.")
                    
                    

main()
