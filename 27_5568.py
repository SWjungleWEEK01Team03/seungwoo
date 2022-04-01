result = []
num = []

def recur(cnum, visit, num_list, count, size):
  global result
  
  if count == 0:
    result.append(cnum)
  else:
    for i in range(0, size):
      if visit[i] == 0:
        visit[i] = 1
        cnum += num[i]
        count -= 1
        recur(cnum, visit, num_list, count, size)
        visit[i] = 0
        cnum = cnum[0:-len(num[i])]
        count += 1

def solve():
  n = int(input())
  k = int(input())
  
  global result
  
  for _ in range(n):
    num.append(input())
  
  for i in range(n):
    visited = [0] * n
    visited[i] = 1
    recur(num[i], visited, num, k-1, n)
  
  result = list(set(result))
  print(len(result))
  
solve()