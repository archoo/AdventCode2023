import itertools,time,functools,math,copy

rawdata = [list(r.strip()) for r in open('day10_test.txt').readlines()]

#dir = {'N':(0,-1),'NE':(1,-1),'E':(1,0),'SE':(1,1),'S':(0,1),'SW':(-1,1),'W':(-1,0),'NW':(-1,-1)}
dir = [(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1)]

        #  [N ,NE,E ,SE,S ,SW,W ,NW]
val = {'|':[1 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ], # is a vertical pipe connecting north and south.
       '-':[0 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ], # is a horizontal pipe connecting east and west.
       'L':[1 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ], # is a 90-degree bend connecting north and east.
       'J':[1 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ], # is a 90-degree bend connecting north and west.
       '7':[0 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ], # is a 90-degree bend connecting south and west.
       'F':[0 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ], # is a 90-degree bend connecting south and east.
       '.':[0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ], # is ground; there is no pipe in this tile.
       'S':[1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ]} # is the starting position of the animal; there is a pipe on this 

con = {'|':[1 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ], # is a vertical pipe connecting north and south.
       '-':[0 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ], # is a horizontal pipe connecting east and west.
       'L':[0 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ], # is a 90-degree bend connecting north and east.
       'J':[0 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ], # is a 90-degree bend connecting north and west.
       '7':[1 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ], # is a 90-degree bend connecting south and west.
       'F':[1 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ], # is a 90-degree bend connecting south and east.
       '.':[0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ], # is ground; there is no pipe in this tile.
       'S':[1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ]} # is the starting position of the animal; there is a pipe on this 


for row in rawdata:
  print(row)

w,h = len(rawdata[0]),len(rawdata)

pmap = copy.deepcopy(rawdata)
    
def lor(l1,l2):
  l3 = []
  for j in l1:
    if j and l2[l1.index(j)]:
      l3.append(1)
    else:
      l3.append(0)    
  return(l3)

for y in range(h):
  for x in range(w):
    v = val[rawdata[y][x]]
    for d in dir:
      if v[dir.index(d)]:
        lu = (x+d[0],y+d[1])
        if lu[0]==-1 or lu[1] == -1 or lu[0] == w or lu[1] == h:
          c = con['.']
        else:
          c = con[rawdata[lu[1]][lu[0]]]
        if sum(lor(v,c)) > 0:
          pmap[y][x] = rawdata[y][x]
        else:
          pmap[y][x] = '.'
    print()
  print()
  
for p in pmap:
  print(p)