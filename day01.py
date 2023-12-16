import re

rawdata = [r.strip() for r in open('day01.txt','rt').readlines()]
sum = 0
digits = {'one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9','zero':'0'}
for row in rawdata:
  num = re.findall('(?=([0-9]|one|two|three|four|five|six|seven|eight|nine|zero))',row,)
  if num[0] in digits.keys():
    n0 = digits[num[0]]
  else: 
    n0 = num[0]
  
  if num[-1] in digits.keys():
    n1 = digits[num[-1]]
  else:
    n1 = num[-1]
  #print(row,num,n0,n1)
  sum += int(n0+n1)

print(sum)