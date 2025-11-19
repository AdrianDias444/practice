'''
Insertion Sort, divide o array tem 2 grupos
- Sorted que comeca com apenas o 1 elemento
- Unsorted que comeca com os restantes
- Pegamos o primeiro elemento do grupo Unsorted e
- comparamos com todos os elementos do grupo Sorted
(da direita para a esquerda), até encontrar a posição correta
- onde ele deve ser inserido.
'''


def insertion_sort(array):
    n = len(array)
    i  = 0
    for i in range(n):
        j = i + 1
        i_temp, j_temp = i, j
        while (array[j_temp] < array[i_temp] and j_temp > 0):
            array[j_temp], array[i_temp] = array[i_temp], array[j_temp]
            j_temp = j_temp - 1
            i_temp = i_temp - 1
        




array = [0, 3, 90, 1, 7, 2, 4, 11]
insertion_sort(array)
for i in range(len(range)):
    print(array[i])
print("array len ", len(array))