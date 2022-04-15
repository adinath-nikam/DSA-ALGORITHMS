import inspect
import os
from Sorting import Menu
from Banners import sorting_banners
from colors import bad, red, yellow, green, white, info, end

# counting sort algorithm
def sort(_list):

    try:
        max_value = 0
        for i in range(len(_list)):
            if _list[i] > max_value:
                max_value = _list[i]

        buckets = [0] * (max_value + 1)

        for i in _list:
            buckets[i] += 1
        i = 0

        for j in range(max_value + 1):
            for a in range(buckets[j]):
                _list[i] = j
                i += 1

        return _list

    except TypeError as error:
        print('Counting Sort can only be applied to integers. {}'.format(error))

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

    sorting_banners.counting_banner()

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