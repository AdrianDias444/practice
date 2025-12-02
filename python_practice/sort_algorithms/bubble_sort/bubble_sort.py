def bubble_sort(array):
    n = len(array)
    trocou = True

    while trocou:
        trocou = False
        i = 0
        while i < n - 1:
            if array[i] > array[i + 1]:
                temp = array[i + 1]
                array[i + 1] = array[i]
                array[i] = temp
                trocou = True
            i = i + 1


array = [0, 3, 90, 1, 7, 2, 4, 11]
bubble_sort(array)
for i in range(len(array)):
    print(array[i])

