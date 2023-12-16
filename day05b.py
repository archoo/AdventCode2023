import math

rawdata = [r.strip() for r in open('day05.txt').readlines() if r.strip() != '']

sr = [int(n) for n in rawdata.pop(0).split(':')[1].split()]
print(sr)
seeds = []
for s in range(0,len(sr),2):
  seeds.append((sr[s],sr[s+1]))
maps = {}

for row in rawdata:
  if ':' in row:
    m = row.split()[0].split('-to-')
    maps[m[0]] = {'to':m[1],'by':[]}
  else:
    data = [int(n) for n in row.split()]
    maps[m[0]]['by'].append([data[1],data[0],data[2]])
    
for m in maps:
  maps[m]['by'].sort()
  fe = maps[m]['by'][0]
  if fe[0] != 0: maps[m]['by'].insert(0,[0,0,fe[0]-1])
  print(m,maps[m])

def lookup(v,m):
  for e in maps[m]['by']:
    if v >= e[0] and v < e[0]+e[2]:
      return e[1] + v-e[0],maps[m]['to'],e[2]-(v-e[0])
  return v,maps[m]['to'],math.inf

closest = math.inf #maps['humidity']['by'][-1][1] + maps['humidity']['by'][-1][2]

for seed,count in seeds:
  print('\n',seed,count,end='')
  c = 0
  while c < count:
    s = seed + c      
    v,m,jump = lookup(s,'seed')
    while m != 'location':
      print(s,m,v,jump)
      v,m,j = lookup(v,m)
      if j < jump: jump = max(1,j)
    print(s,m,v,jump)
    if v < closest: closest = v
    c += jump
    
    
print(closest)
