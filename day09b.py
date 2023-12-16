import itertools,time,functools,math

rawdata = {tuple([int(c) for c in r.strip().split()]):[] for r in open('day09.txt').readlines() if r.strip() != ''}

for row in rawdata:
  nx = tuple([row[i+1]-row[i] for i in range(len(row)-1)])
  while set(nx) != {0}:
    rawdata[row].append(nx)
    nx = tuple([nx[i+1]-nx[i] for i in range(len(nx)-1)])
  rawdata[row].reverse()
  print(row,rawdata[row],end='\n\n')

tot = 0

for row in rawdata:
  seq = rawdata[row]
  i = 0
  for s in seq:
    i = s[0] - i
  i = row[0] - i
  tot += i
  print(row,i)
  
print(tot)