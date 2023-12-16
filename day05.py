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
  print(m,maps[m])

def lookup(v,m):
  for e in maps[m]['by']:
    if v >= e[0] and v < e[0]+e[2]:
      return e[1] + v-e[0],maps[m]['to']
  return v,maps[m]['to']

closest = maps['humidity']['by'][-1][1] + maps['humidity']['by'][-1][2]

for seed,count in seeds:
  print('\n',seed,count,end='')
  c = 0
  while c < count:
    if c % 100000 == 0: print('.',end='',flush=True)
    s = seed + c      
    v,m = lookup(s,'seed')
    while m != 'location':
      #print(s,m,v)
      v,m = lookup(v,m)
    #print(s,m,v)
    if v < closest: closest = v
    c += 1

print(closest)
