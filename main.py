import time
import threading

# Função de merge sort
def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    
    meio = len(nums) // 2
    esquerda = merge_sort(nums[:meio])
    direita = merge_sort(nums[meio:])
    
    return merge(esquerda, direita)

# Função auxiliar para mesclar duas listas ordenadas
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

# Função que será executada por cada thread
def merge_sort_thread(nums, resultado, semaforo):
    nums = merge_sort(nums)
    semaforo.acquire()  # Adquire o semáforo antes de acessar a lista compartilhada
    resultado.append(nums)
    semaforo.release()  # Libera o semáforo após o acesso

# Versão com multithreading usando semáforo
def com_multithreading(nums, num_threads=2):
    inicio = time.time()
    threads = []
    resultado = []
    semaforo = threading.Semaphore()  # Inicializa o semáforo

    # Dividindo a lista de números em partes iguais para cada thread
    tamanho_parte = len(nums) // num_threads
    for i in range(num_threads):
        inicio_parte = i * tamanho_parte
        fim_parte = (i + 1) * tamanho_parte
        parte_nums = nums[inicio_parte:fim_parte]

        # Criando e iniciando a thread
        thread = threading.Thread(target=merge_sort_thread, args=(parte_nums, resultado, semaforo))
        thread.start()
        threads.append(thread)

    # Aguardando todas as threads terminarem
    for thread in threads:
        thread.join()

    # Realizando a operação de merge nas partes ordenadas
    resultado = merge(*resultado)
    
    fim = time.time()
    print("Versão com multithreading e semáforo: Tempo:", fim - inicio, "segundos")

# Versão sem multithreading
def sem_multithreading(nums):
    inicio = time.time()
    resultado = merge_sort(nums)
    fim = time.time()
    print("Versão sem multithreading: Tempo:", fim - inicio, "segundos")

nums = list(range(1000000, 0, -1))

sem_multithreading(nums)
com_multithreading(nums)