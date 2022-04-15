import math
from Sorting import insertion_sort
import inspect
import os
from Sorting import Menu
from Banners import sorting_banners
from colors import bad, red, yellow, green, white, info, end


def sort(_list, bucket_size=5):
    string = False

    if len(_list) == 0:
        return []

    elif all(isinstance(element, str) for element in _list):
        string = True
        _list = [ord(element) for element in _list]

    min_value = _list[0]
    max_value = _list[0]

    # For finding minimum and maximum values
    for i in range(0, len(_list)):
        if _list[i] < min_value:
            min_value = _list[i]
        elif _list[i] > max_value:
            max_value = _list[i]

    # Initialize buckets
    bucket_count = math.floor((max_value - min_value) / bucket_size) + 1
    buckets = []
    for i in range(0, int(bucket_count)):
        buckets.append([])

    # For putting values in buckets
    for i in range(0, len(_list)):
        # TODO: floor expects floats but could be receiving int or slice
        buckets[math.floor(float((_list[i] - min_value) / bucket_size))].append(_list[i])

    # Sort buckets and place back into input array
    sorted_array = []
    for i in range(0, len(buckets)):
        insertion_sort.sort(buckets[i])
        for j in range(0, len(buckets[i])):
            sorted_array.append(buckets[i][j])

    if string:
        return [chr(element) for element in sorted_array]
    else:
        return sorted_array

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

    sorting_banners.bucket_banner()

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