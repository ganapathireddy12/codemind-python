x,y,z=map(int,input().split())
import math
s=(x+y+z)/2
a=math.sqrt(s*(s-x)*(s-y)*(s-z))
print("%.2f" % a)