# Time:      7  15   30
# Distance:  9  40  200
#races = [(7,9),(15,40),(30,200)]

#Time:        49     78     79     80
#Distance:   298   1185   1066   1181
races = [[49,298,0],[78,1185,0],[79,1066,0],[80,1181,0]]

races = [[49787980,298118510661181,0]]

for r in races:
  tm = r[0]
  ds = r[1]
  op = 0
  for a in range(tm+1):
    ch = a
    rc = tm-a
    if ch*rc > ds: op += 1
  r[2] = op
  print(r,op)

import functools
tot = functools.reduce(lambda x,y:x*y,[r[2] for r in races],1)
print(tot)