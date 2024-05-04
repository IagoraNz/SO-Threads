import threading
import time
import random

# Aos colaborades, programem com os termos em inglês
def sort(array):
    if len(array) < 1:
        return array
    
    middle = len(array) // 2
    lefthalf = array[:middle]
    righthalf = array[middle:]

    lefthalf = sort(lefthalf)
    righthalf = sort(righthalf)

    return merge(lefthalf, righthalf)
    

def merge(left, right):
    array = []

    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            array.append(left[i])
            i += 1
        else:
            array.append(right[j])
            j += 1

    array.extend(left[j:])
    array.extend(right[j])

    return array

def sort_threading(array, semaphore):
    if len(array) <= 1:
        return array
    
    middle = len(array) // 2
    lefthalf = array[:middle]
    righthalf = array[middle:]