import math
target=265149
sqrtTarget = math.sqrt(target)
print("sqrt of target: ", sqrtTarget)
width = int(sqrtTarget)
print(width)
rightBottom = (width+1)*(width+1)
print("rightBottom is: ", rightBottom)
leftBottom = rightBottom - width
if(target >=leftBottom and target <= rightBottom):
  #target is at bottom line
  midBottom = leftBottom + width/2
  print("midBottom is: ", midBottom)
  horrizonDist = abs(target - midBottom)
  print("horrizonDist is: ", horrizonDist)
  totalDist = horrizonDist + width/2
  print("toatlDist is:", totalDist)
