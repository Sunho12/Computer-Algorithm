def lis(arr):
    n = len(arr)
 
    h = [1] * n
    p = [-1] * n
    for i in range (1,n):
        for j in range (0,i):
            if arr[i] > arr[j] and h[i] < h[j] +1:
                h[i] = h[j] + 1
                p[i] = j
    
    max_len = max(h)
    end_idx= h.index(max_len)

    lis=[]
    curr = end_idx
    while curr != -1:
        lis.append(arr[curr])
        curr = p[curr]
    lis.reverse()

    return max_len, lis

#test code
arr = [10,22,9,33,21,50,41,60]
length, longest_seq = lis(arr)
print("Length of lis is", length)
print("LIS is ",longest_seq)
