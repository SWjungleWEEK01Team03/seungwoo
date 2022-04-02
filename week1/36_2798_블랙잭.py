import sys

n, m = list(map(int, sys.stdin.readline().split()))

llist = []
llist = list(map(int, sys.stdin.readline().split()))

result = []

def recur(visited, lsum, count):
  if count == 3:
    if lsum <= m:
      result.append(lsum)
    return
  else:
    for i in range(n):
      if visited[i] == 0:
        visited[i] = 1
        count += 1
        lsum += llist[i]
        recur(visited, lsum, count)
        count -= 1
        visited[i] = 0
        lsum -= llist[i]
    
def solution():
  global result
  
  visited = [0] * n
  count = 0
  lsum = 0
  
  recur(visited, lsum, count)
  result = list(set(result))
  print(max(result))
    
  
solution()