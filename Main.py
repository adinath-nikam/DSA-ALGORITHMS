#Importing Required Libraries
import os
from colors import bad, red, yellow, green, white, info, end
#Importing Required Libraries

#Clear the Terminal Screen
os.system('cls')
#Clear the Terminal Screen
def Main_Menu():
    #Just a Fancy Banner
    print('')
    print('%s -------------------- HYPER ALGORITHMS --------------------' %red)
    print('')
    #Just a Fancy Banner
    
    #Menu items in Tuples
    Menu = ('[1] SORTING','[2] SEARCHING','[3] DATA STRUCTURES','[4] GEOMETRY','[5] BINARY','[6] BASIC MATH','[7] PATHFINDING')
    #Menu items in Tuples
    
    #Display Menu items
    for i in range(len(Menu)):
        print(Menu[i])
        #Display Menu items
    
    #Select Option
    option = int(input("Select your option: "))

    if (option == 1):
        os.system('cls')
        from Sorting import Menu
        Menu.sort_menu()
    
    elif (option == 2):
        os.system('cls')
        from Searching import Menu
        Menu.search_menu()
    
    else:
        print('[!] Invalid Operation')
    #Select Option

Main_Menu()