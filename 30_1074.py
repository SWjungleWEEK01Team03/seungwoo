import sys

def solution():
  size, x, y = list(map(int, sys.stdin.readline().split()))  
  
  arr_size = 2 ** size
  num = 0
  
  for _ in range(size):
    half = (arr_size // 2)
    arr_num = ((arr_size) ** 2) // 4
  
    if half <= x and half <= y:
      num += arr_num * 3
      x -= half
      y -= half
    elif half <= x and half > y:
      num += arr_num * 2
      x -= half
    elif half > x and half <= y:
      num += arr_num
      y -= half
      
    arr_size = arr_size // 2
  
  print(num)
  
solution()