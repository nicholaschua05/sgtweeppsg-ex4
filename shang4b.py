line1="1+1"
line2="2-1"
line3="4*5"
line4="4/2"

def calculate(line):
  if '+' in line:
    return int(line[0])+int(line[2])
  elif '-' in line:
    return int(line[0])-int(line[2])
  elif '*' in line:
    return int(line[0])*int(line[2])
  elif '/' in line:
    return int(line[0])/int(line[2])    

print(calculate(line1),calculate(line2),calculate(line3),calculate(line4))