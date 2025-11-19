def selection_short(array):
    n = len(array)

    for i in range(n - 1):
        min = i
        for j in range(i + 1, n):
            if(array[j] < array[min]):
                min = j
        array[i], array[min] = array[min], array[i]

array = [0, 3, 90, 1, 7, 2, 4, 11]
selection_short(array)
for i in range(len(array)):
    print(array[i])