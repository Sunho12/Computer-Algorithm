array = [21, 3, 12, 15, 7, 32, 4, 25, 9, 18]

def quick_sort(array):
    if len(array) <= 1:
        return array 
    pivot = array[len(array) // 2]
    left = []
    right = []
    equal = []
    for num in array:
        if num < pivot:
            left.append(num)
        elif num > pivot:
            right.append(num)
        else:
            equal.append(num)

    return quick_sort(left) + equal + quick_sort(right)

print(quick_sort(array))


