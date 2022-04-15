import os
from Sorting import Menu
from Banners import sorting_banners
from colors import bad, red, yellow, green, white, info, end
import inspect


def sort(_list):
    
    # create the heap
    heapify(_list)              
    end = len(_list) - 1
    while end > 0:
        _list[end], _list[0] = _list[0], _list[end]
        shift_down(_list, 0, end - 1)
        end -= 1
    return _list


def heapify(_list):


    start = len(_list) // 2
    while start >= 0:
        shift_down(_list, start, len(_list) - 1)
        start -= 1


def shift_down(_list, start, end):
    root = start
    while root * 2 + 1 <= end:
        child = root * 2 + 1
        # right child exists and is greater than left child
        if child + 1 <= end and _list[child] < _list[child + 1]:
            child += 1
        # if child is greater than root(parent), then swap their positions
        if child <= end and _list[root] < _list[child]:
            _list[root], _list[child] = _list[child], _list[root]
            root = child
        else:
            return

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

    sorting_banners.heap_banner()

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