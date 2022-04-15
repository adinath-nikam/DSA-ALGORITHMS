import os
from Sorting import Menu
from Banners import sorting_banners
from colors import bad, red, yellow, green, white, info, end
import inspect


def merge(a, b):
    c = []
    while len(a) != 0 and len(b) != 0:
        if a[0] < b[0]:
            c.append(a[0])
            a.remove(a[0])
        else:
            c.append(b[0])
            b.remove(b[0])
    if len(a) == 0:
        c += b
    else:
        c += a
    return c


def sort(_list):
    if len(_list) == 0 or len(_list) == 1:
        return list(_list)
    else:
        middle = len(_list)//2
        a = sort(_list[:middle])
        b = sort(_list[middle:])
        return merge(a, b)

def get_code():
    return inspect.getsource(sort) + "\n" + inspect.getsource(merge)


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

    sorting_banners.merge_banner()

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