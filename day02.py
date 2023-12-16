import re

cubes = {'red':12,'green':13,'blue':14}

rawdata = [r.strip() for r in open('day02.txt').readlines()]

sum = 0

for row in rawdata:
  game = re.search('Game (\d*):',row)[1]
  turns = re.search('Game.*:(.*)',row)[1].split(';')
  poss = True
  for t in turns:
    if (int(re.search('(\d*) green',t)[1]) if re.search('green',t) else 0) > cubes['green']: poss = False
    if (int(re.search('(\d*) red',t)[1]) if re.search('red',t) else 0) > cubes['red']: poss = False
    if (int(re.search('(\d*) blue',t)[1]) if re.search('blue',t) else 0) > cubes['blue']: poss = False
  if poss: sum += int(game)

print(sum)