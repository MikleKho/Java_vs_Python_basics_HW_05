# Реализовать алгоритм пирамидальной сортировки (HeapSort).

import random

def sort_heap(list):

    for start in range(int((len(list) - 2) / 2), -1, -1):
        sieve_heap(list, start, len(list) - 1) 

    for end in range(len(list) - 1, 0, -1): 
        list[end], list[0] = list[0], list[end]
        sieve_heap(list, 0, end - 1)
    return list

def sieve_heap(list, start, end):

    begin = start 

    while True:
        child = begin * 2 + 1

        if child > end: break 
        if child + 1 <= end and list[child] < list[child + 1]:
            child += 1

        if list[begin] < list[child]:
            list[begin], list[child] = list[child], list[begin]
            begin = child
        else:
            break

number_elem = 15
list = [random.randint(10, 99) for i in range(0, number_elem)]
print(f"Исходный список ---> {list}")
sort_heap(list)
print(f"Список после сортировки  ---> {list}")