def insertionSort(a):
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while (j >= 0):
            if a[j] >= key:
                a[j + 1] = a[j]
                j -= 1
            else:
                break
        a[j + 1] = key
    print(a)
if __name__ == "__main__":
    insertionSort([5,3,7,6,11,1,8,4])
            
