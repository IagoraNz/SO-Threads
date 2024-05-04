import threading
import time as tm
import random as rd

def divide(array):
    if len(array) < 1:
        return array
    
    meio = len(array) // 2

    esq = array[:meio]
    dir = array[meio:]

    esq = divide(esq)
    dir = divide(dir)

    return merge(esq, dir)
    

def merge(esq, dir):
    array = []

    i, j = 0, 0

    while i < len(esq) and j < len(dir):
        if esq[i] < dir[j]:
            array.append(esq[i])
            i += 1
        else:
            array.append(dir[j])
            j += 1

    array.extend(esq[i:])
    array.extend(dir[j:])

    return array

def sort_threading(array, semaphore):
    if len(array) <= 1:
        return array
    
    meio = len(array) // 2
    esq = array[:meio]
    dir = array[meio:]

    semaforo_esq = threading.Semaphore(0)
    semaforo_dir = threading.Semaphore(0)

    thread_esq = threading.Thread(target=sort_threading, args=(esq, semaforo_esq))
    thread_dir = threading.Thread(target=sort_threading, args=(dir, semaforo_dir))

    thread_esq.start()
    thread_dir.start()

    thread_esq.join()
    thread_dir.join()

    merge_threading(array, esq, dir, semaforo_esq, semaforo_dir, semaphore)

    semaphore.release()

def merge_threading(array, esq, dir, semaforo_esq, semaforo_dir, semaphore):
    resultado = []

    i, j = 0, 0

    while i < len(esq) and j < len(dir):
        if esq[i] < dir[j]:
            resultado.append(esq[i])
            i += 1
        else:
            resultado.append(dir[j])
            j += 1

    resultado.extend(esq[i:])
    resultado.extend(dir[j:])

    for i in range(len(resultado)):
        array[i] = resultado[i]

    semaforo_esq.release()
    semaforo_dir.release()

def metrifica_normal(array):
    

def main():
    array = [rd.randint(1, 1000) for _ in range(10000)]

