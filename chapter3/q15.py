#15
import math

for deg in range(0, 345, 15)
    sine = round(math.sin(deg), 4)
    cosin = round(math.cos(deg), 4)
    
    print(deg, '---', sine, cosin)