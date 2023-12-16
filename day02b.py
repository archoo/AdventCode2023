import re


rawdata = [r.strip() for r in open('day02.txt').readlines()]

sum = 0

for row in rawdata:
  cubes = {'red':0,'green':0,'blue':0}
  game = re.search('Game (\d*):',row)[1]
  turns = re.search('Game.*:(.*)',row)[1].split(';')
  for t in turns:
    cubes['green'] = max((int(re.search('(\d*) green',t)[1]) if re.search('green',t) else 0),cubes['green'])
    cubes['red'] = max((int(re.search('(\d*) red',t)[1]) if re.search('red',t) else 0),cubes['red'])
    cubes['blue'] = max((int(re.search('(\d*) blue',t)[1]) if re.search('blue',t) else 0),cubes['blue'])
  pow = cubes['green']*cubes['red']*cubes['blue']
  sum += pow
print(sum)