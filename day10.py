import itertools,time,functools,math,copy,os,random
os.system('color')

rawdata = [list(r.strip()) for r in open('day10.txt').readlines()]

dir = {'N':(0,-1),'E':(1,0),'S':(0,1),'W':(-1,0)}
dirc = [(0,-1),(1,0),(0,1),(-1,0)]

        #  [N ,E ,S ,W]
val = {'|':[1 ,0 ,1 ,0], # is a vertical pipe connecting north and south.
       '-':[0 ,1 ,0 ,1], # is a horizontal pipe connecting east and west.
       'L':[1 ,1 ,0 ,0], # is a 90-degree bend connecting north and east.
       'J':[1 ,0 ,0 ,1], # is a 90-degree bend connecting north and west.
       '7':[0 ,0 ,1 ,1], # is a 90-degree bend connecting south and west.
       'F':[0 ,1 ,1 ,0], # is a 90-degree bend connecting south and east.
       '.':[0 ,0 ,0 ,0], # is ground; there is no pipe in this tile.
       'S':[1 ,1 ,1 ,1]} # is the starting position of the animal; there is a pipe on this 

con = {'|':[[1,0,0,0],[0,0,0,0],[0,0,1,0],[0,0,0,0]], # is a vertical pipe connecting north and south.
       '-':[[0,0,0,0],[0,1,0,0],[0,0,0,0],[0,0,0,1]], # is a horizontal pipe connecting east and west.
       'L':[[0,0,0,0],[0,0,0,0],[0,0,1,0],[0,0,0,1]], # is a 90-degree bend connecting north and east.
       'J':[[0,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,0]], # is a 90-degree bend connecting north and west.
       '7':[[1,0,0,0],[0,1,0,0],[0,0,0,0],[0,0,0,0]], # is a 90-degree bend connecting south and west.
       'F':[[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,1]], # is a 90-degree bend connecting south and east.
       '.':[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]], # is ground; there is no pipe in this tile.
       'S':[[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]} # is the starting position of the animal; there is a pipe on this 

# for row in rawdata:
#   print(''.join(row))

w,h = len(rawdata[0]),len(rawdata)

for y in range(h):
  for x in range(w):
    if rawdata[y][x]=='S': start = (x,y)

pmap = copy.deepcopy(rawdata)
pth = []
done = False

def lor(l1,l2):
  l3 = []
  #print(l1,l2,end='')
  for i in range(len(l1)):
    if l1[i] and l2[i]:
      l3.append(1)
    else:
      l3.append(0)    
  #print(l3)
  return(l3)

def cleanup():
  for y in range(h):
    for x in range(w):
      v = val[pmap[y][x]]
      vsum = 0
      for d in dir:
        if v[dirc.index(dir[d])]:
          lu = (x+dir[d][0],y+dir[d][1])
          if lu[0]==-1 or lu[1]==-1 or lu[0]==w or lu[1]==h:
            luv = '.'
          else:
            luv = pmap[lu[1]][lu[0]]
          c = con[luv][dirc.index(dir[d])]
          #print(rawdata[y][x],d,lu,luv,end='')
          vsum += sum(lor(v,c))
      if vsum == 2: pmap[y][x] = rawdata[y][x]
      else: pmap[y][x] = '.'

def navigate(s):
  sx,sy = s
  v = val[pmap[sy][sx]]
  vsum = 0
  vdir = []
  for d in dir:
    if v[dirc.index(dir[d])]:
      lu = (sx+dir[d][0],sy+dir[d][1])
      if lu[0]==-1 or lu[1]==-1 or lu[0]==w or lu[1]==h:
        luv = '.'
      else:
        luv = pmap[lu[1]][lu[0]]
      c = con[luv][dirc.index(dir[d])]
      vsum += sum(lor(v,c))
      if sum(lor(v,c)) == 1:
        vdir.append(lu)      
  if vsum == 2:
    [pth.append(v) for v in vdir if v not in pth[1:]]
  return(pth[-1])

s = navigate(start)
end = pth[0]
pth[0]=start

for y in range(h):
  for x in range(w):
    print(f'\033[{y};{x}H',end='')
    print('\033[31m'+pmap[y][x]+'\033[0m',end='')
  print()
print(f'\033[{start[1]};{start[0]}H',end='')
print('\033[92m'+pmap[start[1]][start[0]]+'\033[0m',end='')
    
while pth[-1] != end:
  print(f'\033[{s[1]};{s[0]}H',end='')
  print('\033[36m'+pmap[s[1]][s[0]]+'\033[0m',end='')
  s = navigate(s)
  
pth.append(start)

def wn(pt,pth):
  wn = 0
  for i in range(len(pth)-1):
    p0,p1 = pth[i],pth[i+1]
    l = ((p1[0] - p0[0]) * (pt[1] - p0[1]) - (pt[0] - p0[0]) * (p1[1] - p0[1]))
    
    if p0[1] <= pt[1]:
      if p1[1] > pt[1]:
        if l > 0: wn += 1
    else:
      if p1[1] <= pt[1]:
        if l < 0: wn -= 1
  return wn

pts = 0
for y in range(h):
  for x in range(w):
    print(f'\033[{y};{x}H',end='')
    if (x,y) in pth:
      print('\033[34m'+pmap[y][x]+'\033[0m',end='')
    else:      
      if wn((x,y),pth)>0: 
        pts += 1
        print('\033[91m'+pmap[y][x]+'\033[0m',end='')
      else:
        print('\033[93m'+pmap[y][x]+'\033[0m',end='')
  print()
  
print(pts)