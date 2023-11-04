def find_minimum_spanning_tree():
    labels = ['1', '2', '3', '4', '5', '6']
    graph = [
        [0, 6.7, 5.2, 2.8, 5.6, 3.6],
        [6.7, 0, 5.7, 7.3, 5.1, 3.2],
        [5.2, 5.7, 0, 3.4, 8.5, 4.0],
        [2.8, 7.3, 3.4, 0, 8, 4.4],
        [5.6, 5.1, 8.5, 8, 0, 4.6],
        [3.6, 3.2, 4, 4.4, 4.6, 0]
    ]
    selected = 0
    v = 6
    selected_arr = [False] * v
    selected_arr[0] = True
    while (selected < v -1):
        min = float('inf')
        from_point = -1
        to_point = -1
        for i in range(v):
            if selected_arr[i]:
                for j in range(v):
                    if not selected_arr[j] and graph[i][j] > 0 and graph[i][j] < min:
                        min = graph[i][j]
                        from_point = i
                        to_point = j
        selected_arr[to_point] = True
        selected += 1
        print(labels[from_point] + " - " + labels[to_point] + " : " + str(graph[from_point][to_point]))
find_minimum_spanning_tree()
