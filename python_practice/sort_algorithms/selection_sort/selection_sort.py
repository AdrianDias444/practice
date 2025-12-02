def selection_sort(array):
    n = len(array)

    for i in range(n):
        min = i
        for j in range(i + 1, n):
            if array[j] < array[min]:
                min = j
        array[i], array[min] = array[min], array[i]


array = [0, 3, 90, 1, 7, 2, 4, 11]
selection_sort(array)
for i in range(len(array)):
    print(i + 1, "Call -", array[i])
print("\nArray len: ", len(array))

