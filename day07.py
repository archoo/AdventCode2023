import re

rawdata = [r.strip().split() for r in open('day07_test2.txt').readlines()]
#rawdata = [r.strip().split() for r in open('day07.txt').readlines()]

hands = [[row[0],int(row[1])] for row in rawdata]
#hands = [('777JJ',1),('JJJ77',1),('7J7J7',1),('J7J7J',1)]

handtypes = {7:'FiveOfaKind',6:'FourOfaKind',5:'FullHouse',4:'ThreeOfaKind',3:'TwoPair',2:'OnePair',1:'SingleCard'}
cards = '23456789TJQKA'

def handtype(h):
  sh = ''.join(sorted(h))
  ht = 0
  s5 = re.findall(r'([AKQJT2-9])\1{4}',sh)
  s4 = re.findall(r'([AKQJT2-9])\1{3}',sh)
  s3 = re.findall(r'([AKQJT2-9])\1{2}',sh)
  s2 = re.findall(r'([AKQJT2-9])\1{1}',sh)
  if s5: ht = 7
  elif s4: ht = 6
  elif s3 and s2 and (s3[0] in s2) and (s3 != s2): ht = 5
  elif s3: ht = 4
  elif len(s2) == 2: ht = 3
  elif len(s2) == 1: ht = 2
  else: ht = 1
  #print(h,sh,s2,s3,s4,s5,handtypes[ht])  
  return ht  

handlist = []

for h in hands:
  hand = h[0]
  rhand = hand
  shand = ''.join(sorted(rhand))
  htype = handtype(rhand)
  crank = [cards.index(c) for c in rhand]
  rank = float(str(htype)+'.'+str(sum(crank)))
  handlist.append([hand,rhand,h[1],shand,htype,crank,rank])
  
#[print(h) for h in handlist]

sortedhands = list(enumerate(sorted(handlist,key=lambda e: (e[4],e[5])),1))

[print(h) for h in sortedhands]

#print(len(set([h[1][2] for h in sortedhands])))

tot = sum([h[0]*h[1][2] for h in sortedhands])
print(tot)