text_01 = "HELLOWORLD"
text_02 = "OHELOD"
arr = []
for i in range(0, len(text_02) + 1):
    arrinside = []
    for j in range(0, len(text_01) + 1):
        arrinside.append(0)
    arr.append(arrinside)
for i in range(1, len(arr)):
    for j in range(1, len(arr[0])):
        if text_01[j - 1] == text_02[i - 1]:
            arr[i][j] = arr[i - 1][j - 1] + 1
        else:
            arr[i][j] = max(arr[i - 1][j], arr[i][j - 1])


arr = arr[1:]
for i in arr:
    i = i[1:]
    print(i)
