import itertools,time,functools,math

rawdata = [r.strip().split(' = ') for r in open('day08.txt').readlines() if r.strip() != '']

st = str(rawdata.pop(0)[0])
st = st.translate(str.maketrans('RL','10'))
st = [int(s) for s in st]

mp = {r[0]:tuple([c.strip() for c in r[1].strip('()').split(',')]) for r in rawdata}

sl = [sp for sp in mp if sp[2] == 'A']
fl = [sp for sp in mp if sp[2] == 'Z']
sc = [0 for l in sl]

print(sl,end=' ')

for cl in sl:
  p = sl.index(cl)
  for s in itertools.cycle(st):
    cl = mp[cl][s]
    sc[p] += 1
    if cl[2] == 'Z': break

print(sc)
print(math.lcm(*sc))
