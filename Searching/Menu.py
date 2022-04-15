#Import Modules
import os
from Searching import linear_search, binary_search, depth_first_search, breadth_first_search
from colors import bad, red, yellow, green, white, info, end

#Import Modules

#Searching Menu
def search_menu():
    print('%s -------------------- SORTING ALGPORITHMS --------------------' %green)
    Search_Algo = ('[1] LINEAR SEARCH','[2] BINARY SORT','[3] BFS SEARCH','[4] DFS SEARCH','[5] INSERTION SORT','[6] MERGE SORT','[7] QUICK SORT','[8] RADIX SORT','[9] SELECTION SORT','[10] SHELL SORT','[11] MAIN MENU (GO  BACK)')
    for i in range(len(Search_Algo)):
        print(Search_Algo[i])

    option = int(input('Select your Option: '))

    if(option == 1):
        linear_search.Main()
    elif(option == 2):
        binary_search.Main()
    elif(option == 3):
        counting_sort.Main()
    elif(option == 4):
        heap_sort.Main()
    elif(option == 5):
        insertion_sort.Main()
    elif(option == 6):
        merge_sort.Main()
    elif(option == 7):
        quick_sort.Main()
    elif(option == 8):
        radix_sort.Main()
    elif(option == 9):
        selection_sort.Main()
    elif(option == 10):
        shell_sort.Main()
    elif(option == 11):
        os.system('cls')
        os.system('py Main.py')

#Searching Menu