import sys


labels = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
From_to = [
  [0, 2, 4, 3, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 7, 4, 6, 0, 0, 0],
  [0, 0, 0, 0, 3, 2, 4, 0, 0, 0],
  [0, 0, 0, 0, 4, 1, 5, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 1, 4, 0],
  [0, 0, 0, 0, 0, 0, 0, 6, 3, 0],
  [0, 0, 0, 0, 0, 0, 0, 3, 3, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
status = []
length = len(labels)
status =  [None] * length
status[length - 1] = {'from' : "", 'to' : "", 'cost' : 0}
for i in range(length - 2, -1, -1):
    status[i] = {'from' : "", 'to' : "", 'cost' : sys.maxsize}
    status[i]['from'] = labels[i]
    for j in range(i + 1, length):
        if From_to[i][j] == 0:
          continue
        print(status[j])
        print(From_to[i][j])
        
        newCost = From_to[i][j] + status[j]['cost']
        if newCost < status[i]['cost']:
          status[i]["cost"] = newCost
          status[i]['to'] = labels[j]

if __name__ == "__main__":
     print(status)
