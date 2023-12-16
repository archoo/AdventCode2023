def put(ch,x,y,col=0):
  print(f'\033[{y};{x}H',end='')
  print(f'\033[{col}m'+ch+'\033[0m',end='')
