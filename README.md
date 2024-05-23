# 📄 Sistemas Operacionais em Multithreading
Repositório colaborativo para desenvolvimento do algoritmo de ordenação Merge Sort na linguagem de programação Python. 
O objetivo é a implantação dos conceitos estudados em Sistemas Operaacionais relacionados ao multithreading e mecanismos de comunicação entre processos.

## :link: Ambiente de desenvolvimento
1. Em relação ao Python
```
Python 3.11.9
```
2. E o Visual Studio Code
```
1.89.1
```
## :link: Objetivo
O algoritmo desenvolvido é uma implementação do algoritmo de ordenação Merge Sort utilizando conceitos avançados de sistemas operacionais, como multithreading, semáforos e mutex. O objetivo é comparar o desempenho do Merge Sort em três cenários distintos: sem multithreading, com multithreading e semáforo, e com multithreading e mutex.

Primeiramente, temos o Merge Sort sem multithreading. Esta é a implementação básica do algoritmo de Merge Sort, que não utiliza threads. Serve como linha de base para medir os ganhos de desempenho nas outras versões que utilizam técnicas de paralelismo. Nesta versão, o algoritmo segue o fluxo tradicional de divisão e conquista, onde o array é dividido recursivamente em sub-arrays até que cada sub-array contenha apenas um elemento, sendo então combinados em ordem crescente.

Em seguida, temos o Merge Sort com multithreading e semáforo. Nesta versão, utilizam-se threads para dividir o trabalho de ordenação em sub-tarefas, permitindo a execução paralela de diferentes partes do array. Além disso, semáforos são utilizados para controlar o número de threads ativas ao mesmo tempo, evitando a sobrecarga do sistema e melhorando a eficiência na utilização dos recursos. Os semáforos garantem que apenas um número limitado de threads possa executar simultaneamente, o que ajuda a manter o equilíbrio na carga de trabalho e na utilização da CPU.

Por fim, o Merge Sort com multithreading e mutex também utiliza threads para paralelizar a ordenação, mas introduz mutexes (Mutual Exclusion) para proteger seções críticas do código onde o acesso simultâneo a recursos compartilhados pode causar problemas. Os mutexes garantem que apenas uma thread por vez pode acessar e modificar determinadas partes do array, evitando condições de corrida. Embora o uso de mutexes possa introduzir um pequeno overhead devido ao controle de acesso, ele assegura a correção e segurança na manipulação de dados compartilhados.

Para avaliar o desempenho das diferentes implementações, consideramos várias métricas. A primeira métrica é o tempo de execução, que mede o tempo total necessário para ordenar o array em cada versão do algoritmo. A segunda métrica é o uso de CPU, que analisa a utilização dos recursos de CPU durante a execução do algoritmo, além de ser avaliado o impacto do hardware nos tempos de execução ao utilizar-se diferentes arquiteturas computacionais para comparar.
