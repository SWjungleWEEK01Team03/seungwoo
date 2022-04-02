x, y = map(int, input().split())

size = int(input())

ax = [x]
ay = [y]

for i in range(0, size):
  xy, l = map(int, input().split())
  if xy == 1:
    ax.append(l)
  else:
    ay.append(l)
    
ax.sort(reverse=True)
ay.sort(reverse=True)
max_x = 0
max_y = 0

if len(ax) > 1:
  ax_temp = []
  for i in range(0, len(ax) - 1):
    ax_temp.append(ax[i] - ax[i+1])
  ax_temp.append(ax[len(ax) - 1])
  max_x = max(ax_temp)
else:
  max_x = x

if len(ay) > 1:
  ay_temp = []
  for i in range(0, len(ay) - 1):
    ay_temp.append(ay[i] - ay[i+1])
  ay_temp.append(ay[len(ay) - 1])
  max_y = max(ay_temp)
else:
  max_y = y
  
print(max_x * max_y)