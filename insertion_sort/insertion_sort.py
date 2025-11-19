"""
Insertion Sort, divide o array tem 2 grupos
- Sorted que comeca com apenas o 1 elemento
- Unsorted que comeca com os restantes
- Pegamos o primeiro elemento do grupo Unsorted e
- comparamos com todos os elementos do grupo Sorted
(da direita para a esquerda), até encontrar a posição correta
- onde ele deve ser inserido.
"""


def insertion_sort(array):
    n = len(array)
    for i in range(n - 1):
        j = i + 1
        while array[j] < array[j - 1] and j > 0:
            array[j], array[j - 1] = array[j - 1], array[j]
            j = j - 1


array = [0, 3, 90, 1, 7, 2, 4, 11]
insertion_sort(array)
for i in range(len(array)):
    print(array[i])
print("array len ", len(array))
