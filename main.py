import time
import threading
import os

def sort(numeros):
    if len(numeros) <= 1:
        return numeros
    
    meio = len(numeros) // 2
    esquerda = sort(numeros[:meio])
    direita = sort(numeros[meio:])
    
    return merge(esquerda, direita)

def merge(esquerda, direita):
    resultado = []
    i = j = 0
    
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1
    
    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    return resultado

def mergesort_thread(numeros, resultado, semaforo):
    numeros = sort(numeros)
    semaforo.acquire()
    resultado.append(numeros)
    semaforo.release()

def multithreading(numeros, num_threads=2):
    inicio = time.time()
    threads = []
    resultado = []
    semaforo = threading.Semaphore()

    tamparte = len(numeros) // num_threads
    for i in range(num_threads):
        inicioparte = i * tamparte
        fimparte = (i + 1) * tamparte
        partenums = numeros[inicioparte:fimparte]

        thread = threading.Thread(target = mergesort_thread, args = (partenums, resultado, semaforo))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    resultado = merge(*resultado)
    
    fim = time.time()
    print(f"\t{fim - inicio:.2f} segundos")

def versaonormal(numeros):
    inicio = time.time()
    sort(numeros)
    fim = time.time()
    print(f"\t{fim - inicio:.2f} segundos")

numeros = list(range(15000000, 0, -1))

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clear()
    print("\tMERGE SORT E MULTITHREADINGS EM EXECUÇÃO")
    print("\n\tTempo de execução do merge sort sem multithreading")
    versaonormal(numeros)
    print("\n\tTempo de execução do merge sort com multithreading e semaforo")
    multithreading(numeros)

if __name__ == "__main__":
    main()