import threading as th
import time as tm
import random as rd

def sort(array):
    if len(array) < 2:
        return array
    
    meio = len(array) // 2

    esq = array[:meio]
    dir = array[meio:]

    esq = sort(esq)
    dir = sort(dir)

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
        semaphore.release()
        return
    
    meio = len(array) // 2
    esq = array[:meio]
    dir = array[meio:]

    semaforo_esq = th.Semaphore(0)
    semaforo_dir = th.Semaphore(0)

    thread_esq = th.Thread(target=sort_threading, args=(esq, semaforo_esq))
    thread_dir = th.Thread(target=sort_threading, args=(dir, semaforo_dir))

    thread_esq.start()
    thread_dir.start()

    thread_esq.join()
    thread_dir.join()

    merge_threading(array, esq, dir, semaforo_esq, semaforo_dir, semaphore)

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
    semaphore.release()

def metrifica_normal(array):
    inicial = tm.time()
    sort(array)
    final = tm.time()
    return final - inicial

def metrifica_threads(array):
    semaforo = th.Semaphore(0)

    inicial = tm.time()
    th.Thread(target=sort_threading, args=(array, semaforo)).start()
    semaforo.acquire()
    final = tm.time()

    return final - inicial

def main():
    array = [rd.randint(1, 1000) for _ in range(10000)]

    print(f"O tempo de ordenação sem threads: {metrifica_normal(array.copy())}")
    print(f"O tempo de execução com multithreading: {metrifica_threads(array.copy())}")

if __name__ == "__main__":
    main()
