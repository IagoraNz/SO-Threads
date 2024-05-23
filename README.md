# 📄 Operating Systems in Multithreading
Collaborative repository for developing the Merge Sort sorting algorithm in the Python programming language. 
The objective is to implement the concepts studied in Operating Systems related to multithreading and communication mechanisms between processes.

## :link: Development environment
1. Regarding Python
```
Python 3.11.9
```
2. Visual Studio Code
```
1.89.1
```
## :link: Project description
**Final grade:** 10/10

The developed algorithm is an implementation of the Merge Sort sorting algorithm using advanced operating system concepts, such as multithreading, semaphores and mutex. The objective is to compare the performance of Merge Sort in three different scenarios: without multithreading, with multithreading and semaphore, and with multithreading and mutex.

Firstly, we have Merge Sort without multithreading. This is the basic implementation of the Merge Sort algorithm, which does not use threads. It serves as a baseline to measure performance gains in other versions that use parallelism techniques. In this version, the algorithm follows the traditional divide and conquer flow, where the array is recursively divided into sub-arrays until each sub-array contains only one element, and then combined in ascending order.

Next we have Merge Sort with multithreading and semaphore. In this version, threads are used to divide the sorting work into sub-tasks, allowing parallel execution of different parts of the array. Furthermore, semaphores are used to control the number of threads active at the same time, avoiding system overload and improving efficiency in resource use. Semaphores ensure that only a limited number of threads can run simultaneously, which helps maintain a balance in workload and CPU utilization.

Finally, Merge Sort with multithreading and mutex also uses threads to parallelize sorting, but introduces mutexes (Mutual Exclusion) to protect critical sections of code where simultaneous access to shared resources can cause problems. Mutexes ensure that only one thread at a time can access and modify certain parts of the array, avoiding race conditions. Although the use of mutexes may introduce a small overhead due to access control, it ensures correctness and security in handling shared data.

To evaluate the performance of different implementations, we consider several metrics. The first metric is execution time, which measures the total time required to sort the array in each version of the algorithm. The second metric is CPU usage, which analyzes the use of CPU resources during the execution of the algorithm, in addition to evaluating the impact of hardware on execution times when using different computational architectures to compare.
