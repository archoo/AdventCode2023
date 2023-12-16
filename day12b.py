import itertools,re,operator,functools

rawdata = [r.strip().split(' ') for r in open('day12_test.txt').readlines()]
folds = 1
tot = 0
for row in rawdata: 
  print(row)
  springs = '?'.join([row[0]] * folds)
  data = springs.replace('.','w').replace('#','b')
  chars = ['bw' if c == '?' else c for c in data]
  print(springs)
  print('combos', functools.reduce(lambda x,y: x*y,[len(c) for c in chars]))
  
  results = row[1].split(',') * folds
  ptrn = '^w*'
  for res in results: 
    ptrn += 'b'*int(res)+'w{1,}'
  ptrn = ptrn[:-5]+'w{0,}$'
  print(ptrn)
  
  rowtot = 0
  for c in itertools.product(*chars):
    if re.match(ptrn,''.join(c)): 
      rowtot += 1
  print(rowtot)
  tot += rowtot

print(tot)