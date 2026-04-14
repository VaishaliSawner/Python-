import math
Peri=36     # Perimeter 
a=10
b=9
c=Peri-a-b 
  
s=Peri/2    #SemiPerimeter

area_Triangle=math.sqrt(s*(s-a)*(s-b)*(s-c))

print(area_Triangle)

