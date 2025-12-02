def double_selection_sort(array):
    i = 0
    j = len(array) - 1
    while i < j:
        min = i
        max = j
        for k in range(i + 1, j + 1):
            if array[min] > array[k]:
                min = k
        array[i], array[min] = array[min], array[i]

        for l in range(j - 1, i - 1, -1):
            if array[max] < array[l]:
                max = l
        array[j], array[max] = array[max], array[j]

        i = i + 1
        j = j - 1


array = [0, 3, 90, 1, 7, 2, 4, 11]
double_selection_sort(array)

for i in range(len(array)):
    print(array[i])
print("Len of array is ", len(array))
