def findSmallest(array):
    smallest = array[0]
    smallest_index = 0
    for i in range(len(array)):
        if array[i] < smallest:
            smallest = array[i]
            smallest_index = i
    return smallest_index


def selectionSort(array):
    new_array = []
    for i in range(len(array)):
        smallest = findSmallest(array)
        new_array.append(array.pop(smallest))
    return new_array