def gnome_sort(array):
    i = 1
    while i < len(array):
        if i == 0:
            i = 1
        j = i - 1
        if array[j] > array[i]:
            array[j], array[i] = array[i], array[j]
            i = i - 1
        else:
            i = i + 1


array = [
    33,
    201,
    89,
    242,
    142,
    199,
    12,
    54,
    161,
    177,
    23,
    212,
    112,
    155,
    188,
    74,
    2,
    44,
    222,
    64,
    92,
    239,
    108,
]
gnome_sort(array)
for i in range(len(array)):
    print(array[i])
