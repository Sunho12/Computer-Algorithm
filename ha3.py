array = [12,3, 6, 1, 99, 3, 34, 25, 21]

def merge(array, start, mid, end):
    n1 = mid-start +1
    n2 = end-mid

    left_arr = array[start:start+n1]
    right_arr = array[mid+1:mid+n2+1]

    l = 0
    r = 0
    k= start
    while l < n1 and r < n2:
        if left_arr[l] <= right_arr[r]:
            array[k] = left_arr[l]
            l += 1
        else:
            array[k] = right_arr[r]
            r += 1
        k += 1
    
    while l < n1 :
        array[k] = left_arr[l]
        l += 1
        k += 1

    while r < n2 :
        array[k] = right_arr[r]
        r += 1
        k += 1

def merge_sort_in_place(array,l,r):
    if (l < r):
        mid = (l + r) // 2
        merge_sort_in_place(array, l, mid)
        merge_sort_in_place(array, mid+1, r)
        merge(array ,l, mid, r)
    

merge_sort_in_place(array, 0, len(array)-1)
print(array)
