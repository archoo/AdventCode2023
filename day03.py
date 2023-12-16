import re

rawdata = [r.strip() for r in open('day03.txt').readlines()]

h,w = len(rawdata),len(rawdata[0])

points = ['N','NE','E','SE','S','SW','W','NW']

def look(y,x,dir):
  match dir:
    case 'N':
      if y == 0: return False
      else: return (rawdata[y-1][x],y-1,x)
    case 'NE':
      if y == 0 or x == w-1: return False
      else: return (rawdata[y-1][x+1],y-1,x+1)
    case 'E':
      if x == w-1: return False
      else: return (rawdata[y][x+1],y,x+1)
    case 'SE':
      if y == h-1 or x == w-1: return False
      else: return (rawdata[y+1][x+1],y+1,x+1)
    case 'S':
      if y == h-1: return False
      else: return (rawdata[y+1][x],y+1,x)
    case 'SW':
      if y == h-1 or x == 0: return False
      else: return (rawdata[y+1][x-1],y+1,x-1)
    case 'W':
      if x == 0: return False
      else: return (rawdata[y][x-1],y,x-1)
    case 'NW':
      if x == 0 or y == 0: return False
      else: return (rawdata[y-1][x-1],y-1,x-1)

parts = []
partlist = []
num = False
tempx = False

for y in range(h):
  for x in range(w):
    if rawdata[y][x].isnumeric(): 
      if num: 
        num = num + rawdata[y][x]
        if x == h-1:
          parts.append([num,(y,tempx),(y,x)])
          num = False
      else: 
        num = rawdata[y][x]
        tempx = x
    else: 
      if num:
        parts.append([num,(y,tempx),(y,x)])
      tempx = False
      num = False
    #print(rawdata[y][x],look(y,x,'N'))

sum = 0

for p in parts:
  valid = False
  py = p[1][0]
  for px in range(p[1][1],p[2][1]):
    for d in points:
      c = look(py,px,d) 
      if c and not(c[0].isnumeric() or c[0] == '.'): 
        valid = True
        p.append(c)
        partlist.append([p[0],p[-1]])
  if valid:
    sum += int(p[0])
  #print(p,valid)
print(sum)

gears = {}
for part,det in partlist:
  if det[0] == '*':
    g = gears.get(det,[])
    g.append(part)
    gears[det] = g

rat = 0
for g,d in gears.items():
  if len(set(d)) == 2:
    gearparts = list(set(d))
    rat += int(gearparts[0])*int(gearparts[1])

print(rat)