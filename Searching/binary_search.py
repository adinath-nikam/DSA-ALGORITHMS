from __future__ import division
import inspect
import os
from Searching import Menu
from Banners import searching_banner
from colors import bad, red, yellow, green, white, info, end


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


def search(_list, target):
    if type(_list) is not list:
        raise TypeError("binary search only excepts lists, not {}".format(str(type(_list))))

    # First position of the list
    left = 0
    # Last position of the list
    right = len(_list) - 1

    try:
        # you can also write while True condition
        while left <= right:
            mid = (left + right) // 2
            if target == _list[mid]:
                return mid
            elif target < _list[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return False
    except TypeError:
        return -1

def get_code():
    return inspect.getsource(search)


def Main():

    os.system('cls')

    searching_banner.binary_banner()

    list_size = int(input('Enter the List Size: '))
    list_elememnts = []
    print('\n Enter List Elements: ')
    for i in range(list_size):
        temp = str(i+1)
        item = int(input('\n Enter '+temp+' Element:'))
        list_elememnts.append(item)


    target_value = int(input("Enter the Number to Search: "))

    list_elememnts.sort()

    
    print('\n LIST: ',list_elememnts)
    print('\n NUMBER TO SEARCH: ',target_value)

    result = search(list_elememnts,target_value)


    if result == False:
        print('\n NUMBER NOT FOUND IN LIST')
    
    else:
        print('\n NUMBER FOUND: True')

    sub_menu()