rawdata = [r.strip().split(':') for r in open('day04.txt').readlines()]
sum=0
cards = {}

for row in rawdata:
  cards[int(row[0][5:])] = row[1].split('|')

print(cards)

for card in cards:
  print(card,end='')
  win,num = cards[card]
  i = 0
  for n in num.split():
    if n in win.split(): 
      i+=1
      print('!',end='')
  sum += pow(2,i-1) if i>0 else 0
  print(pow(2,i-1))
  
print(sum)