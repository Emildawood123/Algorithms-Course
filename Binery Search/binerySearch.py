def binerySearch(array, low, high):
    mid = int((high + low) / 2)
    key = 15
    while(low <= high):
         if key == array[mid]:
            return mid
         elif key > array[mid]:
             low = mid + 1
             mid = int((high + low) / 2)
         elif key < array[mid]:
             high = mid -1
             mid = int((high + low) / 2)
    return -1
if __name__ == "__main__":
    print(binerySearch([1,2,3,4,5,6,7,8,9,10], 0, 9))
