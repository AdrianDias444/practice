def cocktail_shaker_sort(array):
    max = len(array)
    min = 0
    trocou = True
    i = 0
    while trocou:
        trocou = False
        while i < (max - 1):
            j = i + 1
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
                trocou = True
            else:
                i = i + 1
        max = max - 1
        while max > min:
            j = max - 1
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
                trocou = True
            else:
                i = i - 1
        min = min + 1


array = [3, 1, 2, 4, 8, 5]

cocktail_shaker_sort(array)
for i in range(len(array)):
    print(array[i])
