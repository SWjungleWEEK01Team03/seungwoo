import sys
import time

size = int(sys.stdin.readline())

a = [[0]*size]*size

for idx in range(size):
  a[idx] = list(map(int, sys.stdin.readline().split()))

result = sys.maxsize

def recur(start, cur, visited, cost):
  if start == cur and sum(visited) == len(visited):
    print(start, cur, visited)
    global result
    result = min(result, cost)
    return
  for i in range(size):
    if visited[i] == 0 and a[cur][i] != 0:
      visited[i] = 1
      print(cur, i)
      time.sleep(2)
      recur(start, i, visited, cost+a[cur][i])
      print("pop:", i)
      visited[i] = 0

def solution():
  global result
  
  visited = [0] * size
  cost = 0
  recur(0, 0, visited, cost)
  
  print(result)
  
solution()