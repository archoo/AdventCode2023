import re

rawdata = [r.strip().split(':') for r in open('day04.txt').readlines()]
cards = {int(row[0][5:]):row[1].split('|') for row in rawdata}
cardlist = list(range(1,len(cards)+1))
tickets = 0
total = 0

def check(card):
  win,num = cards[card]
  i = 0
  for n in num.split():
    if n in win.split(): 
      i+=1
  return i

while len(cardlist) > 0:
  tickets += 1
  c = cardlist.pop(0)
  w = check(c)
  if w > 0:
    total += pow(2,w-1)
    #cardlist.extend(list(range(c+1,c+1+w)))
  if tickets % 50000 == 0: print('.',end='',flush=True)

print(tickets,total)