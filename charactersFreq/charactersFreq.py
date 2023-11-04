def characterFreq(string):
    arr = [0] * 127
    narr = []
    dic = {}
    for i in range(0, 128):
        for c in string:
            if (c == chr(i)):
                arr[i] += 1
    
    for i in range(0, 127):
        if (arr[i] != 0):
            narr.append([chr(i), arr[i]])
            dic[chr(i)] = arr[i]
    print("by dict: ")
    print(dic)
    # before sort
    print("array before sorting: ")
    print(narr)
    # proccess sort
    sort(narr, 0, len(narr) - 1)
    # after sorting
    print("array after sorting: ")
    print(narr)
# sort funcation
def sort(arr, start, end):
    if end <= start: return
    mid = (end + start) // 2
    sort(arr, start, mid)
    sort(arr, mid + 1, end)
    merge(arr, start, mid, end)
# merge funcation
def merge(arr, start, mid, end):
    l = r = 0
    length_left = (mid - start) + 1
    length_right = (end - mid)
    array_left = [0] * length_left
    array_right = [0] * length_right
    
    for i in range(0, length_left):
        array_left[i] = arr[i + start]
    for j in range(0 , length_right):
        array_right[j] = arr[j + 1 + mid]
    n = start
    while(l < length_left and r < length_right):
        if (array_left[l][1] <= array_right[r][1]):
            arr[n] = array_left[l]
            l +=1
        else:
            arr[n] = array_right[r]
            r +=1
        n += 1
    while (l < length_left):
        arr[n] = array_left[l]
        l +=1
        n +=1
    while (r < length_right):
        arr[n] = array_right[r]
        r +=1
        n +=1

if __name__ == "__main__":
    characterFreq("Hello world")
