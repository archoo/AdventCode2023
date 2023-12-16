import itertools,time,functools,math,copy,os,random
os.system('color')
rawdata = [list(r.strip()) for r in open('day11.txt').readlines()]

def put(ch,x,y,col=0):
  print(f'\033[{y};{x}H',end='')
  print(f'\033[{col}m'+ch+'\033[0m',end='')

dir = {'N':(0,-1),'E':(1,0),'S':(0,1),'W':(-1,0)}
dirc = [(0,-1),(1,0),(0,1),(-1,0)]
w,h = len(rawdata[0]),len(rawdata)

exp = 999999
expy = []
expx = []

for y in range(h-1,0,-1):
  if '#' not in set(rawdata[y]):
    rawdata[y] = list('!'*w)
    expy.append(y)
h = len(rawdata)
  
for x in range(w-1,0,-1):
  col = [row[x] for row in rawdata]
  if '#' not in set(col):
    for y in range(h):
      rawdata[y][x] = '!'
    expx.append(x)
w = len(rawdata[0])

gal = []
for y in range(h):
  for x in range(w):
    match rawdata[y][x]:
      case '#':
        gx,gy = x,y
        for xx in expx:
          if x>xx: gx += exp
        for yy in expy:
          if y>yy: gy += exp
        gal.append((gx,gy))
        put(rawdata[y][x],x,y,33)
      case '!':
        put(rawdata[y][x],x,y,91)
      case '.':
        put(rawdata[y][x],x,y,93)
  print()

galpair = set()
for g1 in gal:
  for g2 in gal:
    if g1 != g2:
      pr = [g1,g2]
      pr.sort()
      galpair.add(tuple(pr))
list(galpair)

tot = 0
for gp in galpair:
  tot += abs(gp[0][0]-gp[1][0])+abs(gp[0][1]-gp[1][1])
print(tot)