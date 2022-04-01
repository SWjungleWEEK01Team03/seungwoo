def isPnum(num):
  count = 0
  
  for i in range(1, num + 1):
    if (num % i) == 0:
      count += 1
    if count > 2:
      return False
  
  if count == 2:
    return True
  
case_size = int(input())

for i in range(0, case_size):
  num = int(input())
  strg = [num//2] * 2

  for k in range(0, num//2):
    if isPnum(strg[0]) == True and isPnum(strg[1]) == True:
      print(strg[0], strg[1])
      break
    
    strg[0] -= 1
    strg[1] += 1