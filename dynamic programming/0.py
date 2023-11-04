items = [{
  "name": "#1",
  "weight": 1,
  "profit": 4
}, {
  "name": "#2",
  "weight": 3,
  "profit": 9
}, {
  "name": "#3",
  "weight": 5,
  "profit": 12
}, {
  "name": "#4",
  "weight": 4,
  "profit": 11
}]

max_weight = 8
items.insert(0, {"name": "#0", "weight": 0, "profit": 0})
dp = [[0 for j in range(max_weight + 1)] for i in range(len(items))]
for i in range(1, len(items)):
    for j in range(1, max_weight + 1):
        if items[i]['weight'] <= j:
            dp[i][j] = max(dp[i-1][j], items[i]["profit"] + dp[i - 1][j - items[i]["weight"]])
        else:
            dp[i][j] = dp[i - 1][j]
print("Max Profit:", dp[len(items) - 1][max_weight])
