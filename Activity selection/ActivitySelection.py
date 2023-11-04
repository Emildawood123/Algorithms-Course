def activity(start, end):
    i = 1
    j = 0
    arr = []
    arr.append([start[0], end[0]])
    while (i < len(start)):
        if (start[i] >= end[j]):
            arr.append([start[i], end[i]])
            j = i
        i+=1
    return (arr)

if __name__ == "__main__":
    print(activity([9,10,11,12,13,15], [11,12,12,14,15,16]))
