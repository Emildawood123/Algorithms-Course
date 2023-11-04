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
    c = start
    for i in range(0, length_left):
        array_left[i] = a[start + i]
    for j in range(0, length_right):
        array_right[j] = a[j + mid + 1]
    for _ in range(0, length_left):
        if (array_left[k] < 0):
            a[c] = array_left[k]
            c +=1
            k +=1
    for _ in range(0, length_right):
        if (array_right[b] < 0):
            a[c] = array_right[b]
            c +=1
            b +=1
    for i in range(k, length_left):
        a[c] = array_left[i]
        c += 1
    for j in range(b, length_right):
        a[c] = array_right[j]
        c += 1
if __name__ == "__main__":
    array = [-5,3,-7,6,-11,1,-8,4]
    print(array)
    mergeSort(array, 0 ,7)
    print(array)
