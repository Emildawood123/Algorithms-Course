class specfic():
    def __init__(self, profit, weight, ratio):
        self.profit = profit
        self.weight = weight
        self.ratio = ratio
    

class fractionalKnap():
    def __init__(self, array):
        self.array = array

    @staticmethod
    def mergeSort(arr, start, end):
        if (start >= end):
            return
        mid = (start + end) // 2
        fractionalKnap.mergeSort(arr, start, mid)
        fractionalKnap.mergeSort(arr, mid+1, end)
        fractionalKnap.merge(arr, start, mid, end)
    @staticmethod
    def merge(arr, start, mid, end):
        r = l = 0
        left_length = (mid - start) + 1
        right_length = end - mid
        left_array = [0] * left_length
        right_array = [0] * right_length
        n = start
        for i in range(0, left_length):
            left_array[i] = arr[i + start]
        for i in range(0, right_length):
            right_array[i] = arr[i + mid + 1]
        while (l < left_length and r < right_length):
            if left_array[l]['ratio'] >= right_array[r]['ratio']:
                arr[n] = left_array[l]
                l += 1
            elif (right_array[r]['ratio'] > left_array[l]['ratio']):
                arr[n] = right_array[r]
                r += 1
            n += 1
        while (l < left_length):
            arr[n] = left_array[l]
            n += 1
            l += 1
        while (r < right_length):
            arr[n] = right_array[r]
            n += 1
            r += 1
        


    def table_to_fill(self):
        arr = []
        for i in range(0, len(self.array)):
             item = specfic(self.array[i][0], self.array[i][1], self.array[i][0] / self.array[i][1])
             arr.append(item.__dict__)
        return arr
    
    @staticmethod
    def bag(wanted, arr):
        table_to_know = []
        for i in arr:
            if (wanted > 0):
                if (wanted >= i['weight']):
                    table_to_know.append(i)
                    wanted = wanted - i['weight']
                elif (wanted < i['weight']):
                    n = {'profit': wanted * i['ratio'], 'weight': wanted, 'ratio': i['ratio']}
                    table_to_know.append(n)
                    break
        print(table_to_know)
                    

            


if __name__ == "__main__":
    okey = fractionalKnap([[4, 1], [9, 2], [12, 10], [11, 4], [6, 3], [5, 5]])
    lorm = okey.table_to_fill()
    fractionalKnap.mergeSort(lorm, 0, len(lorm) - 1)
    fractionalKnap.bag(12, lorm)
