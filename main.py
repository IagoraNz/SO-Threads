import time
import threading
import os

'''
Funcionamento:
    -----------------------------------------------------------------------------------------
    O Merge Sort é um algoritmo de ordenação que segue o paradigma de divisão e conquista.
    A função divide a lista original em duas metades, chama-se recursivamente em cada metade,
    e depois mescla as duas metades ordenadas para produzir a lista final ordenada.
    -----------------------------------------------------------------------------------------
Args:
    numeros (list): Lista de números a serem ordenados.

Returns:
    list: Lista ordenada.
    
'''

def sort(numeros):
    '''
    Função Sort:
        --------------------------------------------------------------------------------------------
        O algoritmo de mergesort é implementado em duas funções, a primeira é a função sort(), que é
        responsável por dividir a lista em duas partes e chamar a função merge() para mesclar as partes
        ordenadas.
        ---------------------------------------------------------------------------------------------
    '''
    
    
    
    # É verificado se a lista possui apenas um elemento, por meio da função len()
    if len(numeros) <= 1:
        # Se a condição for verdadeira, a lista é retornada
        return numeros
    
    # Seguindo o paradigma de divisão e conquista, a lista é dividida em duas partes, para tal, é necessário encontrar o meio da lista
    meio = len(numeros) // 2
    # Novas listas são criadas, uma para a parte da esquerda e outra para a parte da direita
    esquerda = sort(numeros[:meio]) # Parte da esquerda

    direita = sort(numeros[meio:]) # Parte da direita
    
    # As partes ordenadas são mescladas, por meio da função merge()
    return merge(esquerda, direita)

def merge(esquerda, direita):
    '''
    Função Merge:
        ----------------------------------------------------------------------------------------------------
        A função merge() é responsável por mesclar as partes ordenadas da lista, a função recebe duas listas
        como argumentos, a parte da esquerda e a parte da direita.
        ----------------------------------------------------------------------------------------------------
    '''
    
    # Lista para armazenar o resultado da mesclagem
    resultado = []
    # Variáveis para percorrer as listas
    i = j = 0
    # Enquanto i e j forem menores que o tamanho das listas
    while i < len(esquerda) and j < len(direita):
        # Se o elemento da parte da esquerda for menor que o elemento da parte da direita
        if esquerda[i] < direita[j]:
            # O elemento da parte da esquerda é adicionado ao resultado e i é incrementado
            resultado.append(esquerda[i])
            i += 1
        else:
            # Caso contrário, o elemento da parte da direita é adicionado ao resultado e j é incrementado
            resultado.append(direita[j])
            j += 1
    
    # Adiciona os elementos restantes da parte da esquerda e da parte da direita ao resultado
    # A função extend() é utilizada para adicionar vários elementos de uma lista a outra
    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    
    # Retorna o resultado da mesclagem, que é a junção das partes ordenadas
    return resultado
'''
----------------------------------------------------------------------------
Função para executar o algoritmo de mergesort em uma parte dos números
e adicionar o resultado à lista compartilhada "resultado" usando um semáforo
----------------------------------------------------------------------------
'''

'''
O que é um semáforo?
    --------------------------------------------------------------------------
    Semáforos são variáveis especiais que são usadas para controlar o número de
    sinais de acordar a um recurso compartilhado. 
    --------------------------------------------------------------------------

'''
def mergesort_semaforo(numeros, resultado, semaforo):
    # Ordena a parte dos números
    numeros = sort(numeros)
    
    # Adquire o semáforo para garantir exclusão mútua ao acessar "resultado"
    # Um semáforo é uma variável especial usada para controlar o acesso a um recurso compartilhado.
    # Ele mantém um contador que rastreia quantos "sinais" estão disponíveis.
    # Quando o contador é maior que zero, uma thread pode adquirir (diminuir o contador) o semáforo.
    # Quando o contador é zero, a thread deve esperar até que o semáforo seja liberado.
    # Aqui, acquire() diminui o contador do semáforo. Se o contador chegar a zero,
    # a thread espera até que outra thread chame release() para incrementar o contador.
    semaforo.acquire()
    
    # Adiciona a parte ordenada dos números à lista "resultado"
    # A variável "resultado" é um recurso compartilhado entre várias threads.
    # Para evitar que múltiplas threads modifiquem "resultado" simultaneamente
    # e causem condições de corrida (race conditions), o acesso a "resultado"
    # é protegido pelo semáforo.
    resultado.append(numeros)
    
    # Libera o semáforo para permitir que outras threads o utilizem
    # Após terminar de modificar "resultado", a thread chama release() para
    # incrementar o contador do semáforo, sinalizando que outras threads podem adquirir
    # o semáforo e acessar "resultado".
    semaforo.release()

'''
-------------------------------------------------------------------------
Função para executar o algoritmo de mergesort em uma parte dos números
e adicionar o resultado à lista compartilhada "resultado" usando um mutex
-------------------------------------------------------------------------
'''
def mergesort_mutex(numeros, resultado, lock):
    # Ordena a parte dos números
    numeros = sort(numeros)
    # Bloqueia o mutex para garantir exclusão mútua ao acessar "resultado"
    lock.acquire() #mutex_lock - invocada quando um thread (ou processo) precisa de
                   # acesso a uma região crítica. 

    # Adiciona a parte ordenada dos números à lista "resultado"
    resultado.append(numeros)
    # Libera o mutex para permitir que outras threads o utilizem
    lock.release() #mutex_unlock - quando o thread concluiu o uso da região crítica e
                   # deseja sair.

'''
--------------------------------------------------------------------
Função que realiza o mergesort com múltiplas threads usando semáforo
--------------------------------------------------------------------
'''
def multithreading_semaforo(numeros, num_threads=2):
    # Registra o tempo de início da execução
    inicio = time.time()
    # Lista para armazenar as threads
    threads = []
    # Lista para armazenar os resultados das partes ordenadas
    resultado = []
    # Cria um semáforo
    semaforo = threading.Semaphore() # A função Semaphore() cria um semáforo com um contador inicial de 1

    # Divide a lista de números em partes iguais para cada thread
    tamparte = len(numeros) // num_threads
    for i in range(num_threads):
        inicioparte = i * tamparte
        fimparte = (i + 1) * tamparte
        partenums = numeros[inicioparte:fimparte]

        # Cria uma nova thread para executar a função mergesort_semaforo, passando como argumentos
        # a parte dos números que a thread deve ordenar, a lista compartilhada "resultado"
        # onde o resultado ordenado será armazenado, e o semáforo para controlar o acesso à lista compartilhada.
        thread = threading.Thread(target=mergesort_semaforo, args=(partenums, resultado, semaforo))
        
        # Inicia a execução da thread criada.
        thread.start()
        
        # Adiciona a thread à lista de threads para que possamos monitorar e aguardar
        # a conclusão de todas as threads posteriormente.
        threads.append(thread)


    # Espera todas as threads terminarem
    for thread in threads:
        thread.join()

    # Junta os resultados das threads e realiza o merge final
    resultado = merge(*resultado)
    
    # Registra o tempo de fim da execução
    fim = time.time()
    # Imprime o tempo total de execução
    print(f"\t{fim - inicio:.2f} segundos")

'''
-----------------------------------------------------------------
Função que realiza o mergesort com múltiplas threads usando mutex
-----------------------------------------------------------------
'''
def multithreading_mutex(numeros, num_threads=2):
    '''
    -----------------------------------------------
    Mutexes são versões simplificadas de semáforos.
    -----------------------------------------------
    - são usados quando a capacidade do semáforo de fazer contagem não é necessária.
    - fáceis e eficientes de implementar.
    - Variável compartilhada que pode estar em um de dois estados:
      destravado ou travado.
    - Duas rotinas: mutex_lock e mutex_unlock.
    =================================================================================
    '''
    # Registra o tempo de início da execução
    inicio = time.time()
    # Lista para armazenar as threads
    threads = []
    # Lista para armazenar os resultados das partes ordenadas
    resultado = []
    # Cria um lock (mutex) para garantir exclusão mútua ao acessar "resultado"
    lock = threading.Lock()

    # Divide a lista de números em partes iguais para cada thread
    tamparte = len(numeros) // num_threads
    for i in range(num_threads):
        inicioparte = i * tamparte
        fimparte = (i + 1) * tamparte
        partenums = numeros[inicioparte:fimparte]

        # Cria e inicia a thread, passando a parte dos números, a lista compartilhada
        # e o mutex como argumentos
        thread = threading.Thread(target=mergesort_mutex, args=(partenums, resultado, lock))
        

        # Inicia a execução da thread criada.
        thread.start()

        # Adiciona a thread à lista de threads para que possamos monitorar e aguardar
        # a conclusão de todas as threads posteriormente.
        threads.append(thread)

    # Espera todas as threads terminarem
    for thread in threads:
        thread.join()

    # Junta os resultados das threads e realiza o merge final
    resultado = merge(*resultado)
    
    fim = time.time()
    print(f"\t{fim - inicio:.2f} segundos")


'''
---------------------------------------------
Função que realiza o mergesort sem multhreads
---------------------------------------------
'''
def versaonormal(numeros):
    # Registra o tempo de início da execução
    inicio = time.time()
    # Chama a função de ordenação
    sort(numeros)
    # Registra o tempo de fim da execução
    fim = time.time()
    # Imprime o tempo total de execução
    print(f"\t{fim - inicio:.2f} segundos")

def clear():
    # Limpa o console
    os.system('cls' if os.name == 'nt' else 'clear')

# Função principal
def main():
    print("\n\tGerando a lista de números...")
    numeros = list(range(15000000, 0, -1))
    clear()
    print("\tMERGE SORT E MULTITHREADINGS EM EXECUÇÃO")
    print("\n\tTempo de execução do merge sort sem multithreading")
    versaonormal(numeros)
    print("\n\tTempo de execução do merge sort com multithreading e semáforo")
    multithreading_semaforo(numeros)
    print("\n\tTempo de execução do merge sort com multithreading e mutex")
    multithreading_mutex(numeros)

if __name__ == "__main__":
    main()
