import os
from Sorting import Menu
from Banners import sorting_banners
from colors import bad, red, yellow, green, white, info, end
import inspect

def sort(_list):
    if len(_list) <= 1:
        return list(_list)
    pivot = _list[len(_list) // 2]
    left = [x for x in _list if x < pivot]
    middle = [x for x in _list if x == pivot]
    right = [x for x in _list if x > pivot]
    return sort(left) + middle + sort(right)

def get_code():
    return inspect.getsource(sort)


def sub_menu():

    print('\nEnter 66 to View the Bubble Sorting Algorithm')
    print('Enter 77 for Sorting Menu')
    print('Enter 88 for Main Menu')

    option = int(input())

    if(option == 66):
        os.system('cls')
        print(get_code())
        sub_menu()
    elif(option == 77):
        os.system('cls')
        Menu.sort_menu()
    elif(option == 88):
        os.system('cls')
        os.system('py Main.py')


def Main():

    os.system('cls')

    sorting_banners.quick_banner()

    list_size = int(input('Enter the List Size: '))
    list_elememnts = []
    print('\n Enter List Elements: ')
    for i in range(list_size):
        temp = str(i+1)
        item = int(input('\n Enter '+temp+' Element:'))
        list_elememnts.append(item)
    
    print('\n UN-SORTED LIST: ',list_elememnts)
    
    unsortedlist = list_elememnts
    sorted_list = sort(unsortedlist)
    print('\n SORTED LIST: ',sorted_list)

    sub_menu()