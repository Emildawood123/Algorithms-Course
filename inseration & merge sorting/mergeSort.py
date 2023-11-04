def mergeSort(a, start, end):
    if end <= start:
        return
    mid = (start + end) // 2
    mergeSort(a, start, mid)
    mergeSort(a, mid + 1, end)
    merge(a, start, mid, end)

def merge(a, start, mid, end):
    k = b = 0
    
    length_left = mid - start + 1
    length_right= end - mid
    array_left = [0] * length_left
    array_right  = [0] * length_right
    for i in range(0, length_left):
        array_left[i] = a[start + i]
    for j in range(0, length_right):
        array_right[j] = a[mid + 1 + j]
    c = start
    while (k < length_left and b < length_right):
        if (array_left[k] <= array_right[b]):
            a[c] = array_left[k]
            k +=1
        else:
            a[c] = array_right[b]
            b += 1
        c +=1
    while (k < length_left):
        a[c] = array_left[k]
        c +=1
        k +=1
    while (b < length_left):
        a[c] = array_right[b]
        c +=1
        b +=1
if __name__ == "__main__":
    array = [5,3,7,6,11,1,8,4]
    print(array)
    mergeSort(array, 0 ,7)
    print(array)
