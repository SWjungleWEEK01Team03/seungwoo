size = int(input())

a = [[0]*size]*size

for idx in range(size):
  a[idx] = list(map(int, input().split()))
  
result = []

def calc(cost):
  global result
  
  rcost = 0
  
  for idx in range(size - 1):
    rcost += a[cost[idx]][cost[idx+1]]
    
  rcost += a[cost[len(cost) - 1]][cost[0]]
  result.append(rcost)

def recur(visited, cost, count):
  global result
  
  if count == size:
    calc(cost)
    return
  for i in range(size):
    if visited[i] == 0:
      visited[i] = 1
      cost.append(i)
      recur(visited, cost, count+1)
      visited[i] = 0
      cost.pop()
      
def solution():
  global result
  
  visited = [0] * size
  cost = []
  count = 0
  recur(visited, cost, count)
  
  print(min(result))
  
solution()