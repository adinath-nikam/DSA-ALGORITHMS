import inspect
import os
from Searching import Menu
from Banners import searching_banner
from colors import bad, red, yellow, green, white, info, end


def search(_list, target, initial_position=0):
    position = initial_position
    while position < len(_list):
        if target == _list[position]:
            return position+1
        position += 1
    return -1

def get_code():
    return inspect.getsource(search)

def sub_menu():

    print('\nEnter 66 to View the Bubble Sorting Algorithm')
    print('Enter 77 for Searching Menu')
    print('Enter 88 for Main Menu')

    option = int(input())

    if(option == 66):
        os.system('cls')
        print(get_code())
        sub_menu()
    elif(option == 77):
        os.system('cls')
        Menu.search_menu()
    elif(option == 88):
        os.system('cls')
        os.system('py Main.py')


def Main():

    os.system('cls')

    searching_banner.linear_banner()

    list_size = int(input('Enter the List Size: '))
    list_elememnts = []
    print('\n Enter List Elements: ')
    for i in range(list_size):
        temp = str(i+1)
        item = int(input('\n Enter '+temp+' Element:'))
        list_elememnts.append(item)

    target_value = int(input("Enter the Number to Search: "))
    
    print('\n LIST: ',list_elememnts)
    print('\n NUMBER TO SEARCH: ',target_value)

    result = search(list_elememnts,target_value)

    if result == -1:
        print('\n NUMBER NOT FOUND IN LIST')
    
    else:
        print('\n NUMBER FOUND AT LOCATION: ',result)

    sub_menu()