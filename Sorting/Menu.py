#Import Modules
import os
from Sorting import bubble_sort, bucket_sort, insertion_sort, counting_sort, heap_sort, merge_sort, quick_sort, radix_sort, selection_sort, shell_sort
from colors import bad, red, yellow, green, white, info, end

#Import Modules

#Sorting Menu
def sort_menu():
    print('%s -------------------- SORTING ALGPORITHMS --------------------' %green)
    Sort_Algo = ('[1] BUBBLE SORT','[2] BUCKET SORT','[3] COUNTING SORT','[4] HEAP SORT','[5] INSERTION SORT','[6] MERGE SORT','[7] QUICK SORT','[8] RADIX SORT','[9] SELECTION SORT','[10] SHELL SORT','[11] MAIN MENU (GO  BACK)')
    for i in range(len(Sort_Algo)):
        print(Sort_Algo[i])

    option = int(input('Select your Option: '))

    if(option == 1):
        bubble_sort.Main()
    elif(option == 2):
        bucket_sort.Main()
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

#Sorting Menu